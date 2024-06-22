import platform

from LinuxSystemClock import *
from WindowsSystemClock import *


def create_system_clock():
    platform_name = platform.system()

    if platform_name == 'Windows':
        return WindowsSystemClock()
    elif platform_name == 'Linux':
        return LinuxSystemClock()

    return None
