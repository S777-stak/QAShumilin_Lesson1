class Truck:
    def __init__(self):
        self.__str = "str"

    def __output(self, item, output=None) -> str:
        str = ""
        for key, value in self.__dict__.items():
            str += f"{self.__output(key)}: {value}"
        return output

    def __str__(self):
        return (
            f"{self.__class__.__name__}:{{\n"
            f"\n\t{str}\n}}"
        )