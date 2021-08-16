from SergeyShumilin.QAShumilin_Lesson1.truck_singleton import singleton


@singleton
class Truck:
    def __init__(self, color: str, wheel_size: int):
        self.__color = color
        self.__wheel_size = wheel_size
        self.__electro = False


if __name__ == '__main__':
    truck_1 = Truck("Black", 50)
    truck_2 = Truck("Brown", 50)
    print()