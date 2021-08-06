from SergeyShumilin.QAShumilin_Lesson1.truck import Truck

if __name__ == '__main__':
    truck = Truck()
    print(truck.load_status)
    truck.start_load()
    print(truck.load_status)
    print(truck.get_coordinates())
    truck.move_cargo("up", 5)
    print(truck.get_coordinates())
    truck.move_cargo("forward", 10)
    print(truck.get_coordinates())

