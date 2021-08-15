from Lesson_15.product_store import ProductStore

class CelleryStore(ProductStore):
    _product_type = "Cellery"

    def __init__(self):
        self.__name = "Cell"
        self.__positions = ["Cell", "Super"]

    @property
    def positions(self):
        return self.__positions

    def get_product(self, name: str):
        if name == "Cell":
            return "Cell"