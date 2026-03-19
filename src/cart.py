class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = {}

    def add_item(self, sku, qty):
        if qty <= 0: raise ValueError()
        if not self.catalog.get_by_sku(sku): raise ValueError("Not in catalog")
        self.items[sku] = self.items.get(sku, 0) + qty

    def get_total(self):
        return sum(self.catalog.get_by_sku(sku).price * qty for sku, qty in self.items.items())
        
