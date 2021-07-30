from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, engine_power: int, body_volume: int, number_seats: int):
        self.engine_power = engine_power
        self.body_volume = body_volume
        self.number_seats = number_seats

    @abstractmethod
    def do_carry_passengers(self):
        raise NotImplementedError("Not implemented")

class Passenger_car(Vehicle):
    def __init__(self):
        super().__init__(2000, 2000, 10)

    def do_carry_passengers(self):
        print("it is Passenger_car")


if __name__ == '__main__':
    mersedes = Passenger_car()
    mersedes.do_carry_passengers()