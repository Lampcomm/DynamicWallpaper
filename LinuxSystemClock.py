import os
from SystemClock import *


class LinuxSystemClock(SystemClock):
    def __init__(self):
        self.time_acquisition_command = r"date +%R"

    def _now_impl(self) -> Time:
        system_time = self.__get_system_time()
        return self.__parse_system_time(system_time)

    def __get_system_time(self):
        time_str = os.popen(self.time_acquisition_command).read()
        return time_str

    def __parse_system_time(self, time_str: str) -> Time:
        hour, minute = map(int, time_str.split(":"))
        return Time(hour, minute)
