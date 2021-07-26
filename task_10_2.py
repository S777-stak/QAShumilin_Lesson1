class Employee:
    """Базовый класс сотрудника"""
    name = []
    age = []
    position = []
    salary = []
    address = []

    """Конструктор класса"""
    def __init__(
        self,
        name: str = None,
        age: int = None,
        position: str = None,
        salary: int = None,
        address: str = None,
    ):
        self.__name = name
        self.__position = position
        self.__salary = salary
        self.__age = age
        self.__address = address

    """Метод отображения сотрудника"""
    def display_employee(self, __name, __age):
        return self.__name
        return self.__age

    """Метод отображения отображения атрибутов name  и  age"""
    @classmethod
    def from_name_and_age(cls, __name, __age):
        return cls(__name, __age)

    """Модификация name"""
    @property
    def name(self):
        return self.__name

    """Доступ к модификации name"""
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

if __name__ == '__main__':
    john = Employee("John", 30)
    print(john.name)
    john.name = "Josef"
    print(john.name)