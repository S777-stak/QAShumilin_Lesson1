from .carrying import ICarrying
from .traveling import ITraveling


class Truck(ICarrying, ITraveling):
    def __init__(self):
        self.number_of_bodies = 2
        self.number_of_motors = 2
        self.__load_status = False
        self.__x = 0
        self.__y = 0
        self.__z = 0
        self.__whole_load = 100
        self.__is_on_body = True

    def pull_the_load(self):
        pass

    def move_cargo(self, direction: str, distance: int):
        pass

    def drop_a_load(self):
        pass

    def drive_fast(self):
        pass

    def drive_slow(self):
        pass

    def start_load(self):
        pass

    def start_load(self):
        self.__load_status = True

    def move_cargo(self, direction: str, distance: int):
        if direction == "up":
            self.__z += distance
            if self.__is_on_body:
                self.__is_on_body = False
        elif direction == "down":
            if self.__z > 0:
                self.__z -= distance
        elif direction == "right":
            self.__x += distance
        elif direction == "left":
            self.__x -= distance
        elif direction == "forward":
            self.__y += distance
        elif direction == "back":
            self.__y -= distance
        else:
            pass

    def drop_a_load(self):
        self.__load_status = False
        if not self.__is_on_body:
            self.drop_a_load()

    @property
    def load_status(self):
        return self.__load_status

    def get_coordinates(self) -> tuple:
        return self.__x, self.__y, self.__z

