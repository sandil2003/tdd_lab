class Product:
    def __init__(self, sku, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.sku, self.name, self.price = sku, name, price

class Catalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.sku] = product

    def get_by_sku(self, sku):
        return self.products.get(sku)