class Vehicle:
    def __init__(self, engine_power: int, body_volume: int, number_seats: int):
        self.engine_power = engine_power
        self.body_volume = body_volume
        self.number_seats = number_seats

    def Carry_cargo(self):
        print("Vehicle can carry cargo")


class Truck(Vehicle):
    def __init__(self, engine_power: int, body_volume: int, number_seats: int,
                 carrying_capacity: int):
        super().__init__(engine_power, body_volume, number_seats)
        self.carrying_capacity = carrying_capacity

    def Carry_cargo(self):
        """
            Provide basic carry_cargo from Vehicle and additional possibility
        """

        super().Carry_cargo()
        print("Truck also additionally carry cargo"
              "like monster)")


if __name__ == '__main__':
    DAFF = Truck(5000, 3000, 3, 1500)
    DAFF.Carry_cargo()


