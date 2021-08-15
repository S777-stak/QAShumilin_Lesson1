from Lesson_15.product_store import ProductStore

class AppleStore(ProductStore):
    _product_type = "Apple"

    def __init__(self):
        self.__name = "Juice"
        self.__positions = ["Juice", "Super"]

    @property
    def positions(self):
        return self.__positions

    def get_product(self, name: str):
        if name == "Juice":
            return "Juice"