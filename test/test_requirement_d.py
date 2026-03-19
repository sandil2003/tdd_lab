import pytest
from src.catalog import Product, Catalog
from src.cart import Cart

def test_bulk_discount_applied_at_10_units():
    catalog = Catalog()
    # $100 item. 10 units = $1000 raw. 10% bulk discount = $900 total.
    catalog.add_product(Product("BULK-01", "SSD", 100.0))
    
    cart = Cart(catalog)
    cart.add_item("BULK-01", 10)
    
    # This will fail because our current get_total() doesn't know about discounts
    assert cart.get_total() == 900.0

def test_order_discount_applied_over_1000():
    catalog = Catalog()
    # $1200 raw. No bulk discount. 5% order discount = $1140 total.
    catalog.add_product(Product("HIGH-01", "Monitor", 1200.0))
    
    cart = Cart(catalog)
    cart.add_item("HIGH-01", 1)
    
    assert cart.get_total() == 1140.0