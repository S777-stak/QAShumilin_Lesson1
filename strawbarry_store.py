from Lesson_15.product_store import ProductStore

class StrawbarryStore(ProductStore):
    _product_type = "Strawbarry"

    def __init__(self):
        self.__name = "Straw"
        self.__positions = ["Straw", "Super"]

    @property
    def positions(self):
        return self.__positions

    def get_product(self, name: str):
        if name == "Straw":
            return "Straw"