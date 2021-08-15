from Lesson_15.product_store import ProductStore
from Lesson_15.apple_store import AppleStore
from Lesson_15.banana_store import BananaStore
from Lesson_15.cellery_store import CelleryStore
from Lesson_15.strawbarry_store import StrawbarryStore

class Market:
    @staticmethod
    def get_store(product_type: str) -> ProductStore:
        if product_type == "Apple":
            return AppleStore()
        elif product_type == "Banana":
            return BananaStore()
        elif product_type == "Cellery":
            return CelleryStore()
        elif product_type == "Strawbarry":
            return StrawbarryStore()
        else:
            raise Exception("Incorrect name of product")

if __name__ == '__main__':
    store = Market.get_store("Apple")
    print(store.get_product("Juice"))