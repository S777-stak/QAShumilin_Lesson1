class Toshiba:
    """Базовый класc компании"""
    name = []
    profit = []
    rating = []
    size = []
    address = []

    """Конструктор класса"""
    def __init__(
        self,
        name: str = None,
        profit: int = None,
        rating: str = None,
        size: int = None,
        address: str = None,
    ):
        self.__name = name
        self.__profit = profit
        self.__rating = rating
        self.__size = size
        self.__address = address

    """Метод отображения сотрудника"""
    def display_employee(self, __name, __profit):
        return self.__name
        return self.__profit

    """Метод отображения отображения атрибутов name  и  profit"""
    @classmethod
    def from_name_and_profit(cls, __name, __profit):
        return cls(__name, __profit)

    """Модификация name"""
    @property
    def name(self):
        return self.__name

    """Доступ к модификации name"""
    @name.setter
    def name(self, new_name: str) -> None:
        self.__name = new_name

if __name__ == '__main__':
    company = Toshiba("New_Toshiba", 300000000)
    print(company.name)
