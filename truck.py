class Truck:
    def __init__(self):
        self.__speed = 100
        self.__weight = 1500

    # TODO not clear purpose of this method
    def __output(self, item, output=None) -> str:
        str = ""
        for key, value in self.__dict__.items():
            str += f"{self.__output(key)}: {value}"
        return output

    def __str__(self):
        # TODO: you should iterate __dict__ here and update keys to get expected view
        # for key, value in self.__dict__.........
        return (
            f"{self.__class__.__name__}:{{\n"
            f"\n\t{str}\n}}"
        )

# Good. IT is works but only with 1 field. What if I will add more fields?
# Actual: Truck:{
#
# 	<class 'str'>
# }

# Expected: Truck:{
#     max_speed: 100,
#     weight: 1500
# }