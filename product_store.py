from abc import ABC, abstractmethod

class ProductStore(ABC):
    _product_type: str = ""

    @abstractmethod
    def get_product(self, name: str):
        pass