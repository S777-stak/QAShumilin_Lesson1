from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, engine_power: int, body_volume: int, number_seats: int):
        self.engine_power = engine_power
        self.body_volume = body_volume
        self.number_seats = number_seats

    @abstractmethod
    def do_carry_passengers(self):
        raise NotImplementedError("Not implemented")


class Electro_car(Vehicle):
    def __init__(self):
        super().__init__(1000, 1000, 2)

    def _carries_passengers(self):
        print("carries_passengers...")

    def __charging(self):
        print("Charging...")

    def takes_long_time_charge(self):
        """does_not_breake"""
        self.__charging()

class Passenger_car(Vehicle):
    def __init__(self):
        super().__init__(1000, 1000, 3)

    def do_carry_passengers(self):
        print("it is just Passenger_car")
        self._carries_passengers()


if __name__ == '__main__':
    Nissan_leaf = Passenger_car()
    Nissan_leaf.carries_passengers()
    Nissan_leaf.takes_long_time_charge()
