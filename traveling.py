from abc import ABC, abstractmethod


class ITraveling(ABC):
    @abstractmethod
    def drive_fast(self):
        """Declare drive_fast behaviour for child classes"""
        pass

    @abstractmethod
    def drive_slow(self):
        """Declare drive_slow behaviour for child classes"""
        pass

