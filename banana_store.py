from Lesson_15.product_store import ProductStore

class BananaStore(ProductStore):
    _product_type = "Banana"

    def __init__(self):
        self.__name = "Equdor"
        self.__positions = ["Equdor", "Super"]

    @property
    def positions(self):
        return self.__positions

    def get_product(self, name: str):
        if name == "Equdor":
            return "Equdor"