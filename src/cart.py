class Cart:
    def __init__(self, catalog, inventory_service):
        self.catalog = catalog
        self.inventory = inventory_service
        self.items = {}

    def add_item(self, sku, qty):
        if qty <= 0: raise ValueError("Quantity must be > 0")
        if self.inventory:
            available = self.inventory.get_available(sku)
            if qty > available:
                raise PermissionError("Insufficient inventory")

        if not self.catalog.get_by_sku(sku): raise ValueError("Not in catalog")
        self.items[sku] = self.items.get(sku, 0) + qty

    def get_total(self):
        return sum(self.catalog.get_by_sku(sku).price * qty for sku, qty in self.items.items())

