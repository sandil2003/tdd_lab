class Product:
    """Represents a product in the catalog."""
    def __init__(self, sku: str, name: str, price: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.sku: str = sku
        self.name: str = name
        self.price: float = price

class Catalog:
    """An inventory system to manage and retrieve products by SKU."""
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        """Adds a product to the catalog."""
        self.products[product.sku] = product

    def get_by_sku(self, sku: str) -> Product | None:
        """Retrieves a product if found otherwise None"""
        return self.products.get(sku)