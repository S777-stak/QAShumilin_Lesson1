from abc import ABC, abstractmethod


class ICarrying(ABC):
    @abstractmethod
    def pull_the_load(self):
        pass

    @abstractmethod
    def move_cargo(self, direction: str, distance: int):
        pass

    @abstractmethod
    def drop_a_load(self):
        pass
