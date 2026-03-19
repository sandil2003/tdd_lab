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

def get_total(self) -> float:
    subtotal = 0.0
    bulk_discount = 0.0

    for sku, qty in self.items.items():
        product = self.catalog.get_by_sku(sku)
        line_price = product.price * qty
        
        if qty >= 10:
            bulk_discount += line_price * 0.10
        
        subtotal += line_price

    total_after_bulk = subtotal - bulk_discount

    order_discount = 0.0
    if total_after_bulk >= 1000:
        order_discount = total_after_bulk * 0.05

    return total_after_bulk - order_discount
