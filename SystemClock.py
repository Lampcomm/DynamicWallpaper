from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Time:
    hour: int
    minute: int


class SystemClock(ABC):
    def now(self) -> Time:
        return self._now_impl()

    @abstractmethod
    def _now_impl(self) -> Time:
        pass
