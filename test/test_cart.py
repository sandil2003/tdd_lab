import pytest
from src.cart import Cart
from src.catalog import Catalog, Product

def test_cart_total():
    cat = Catalog()
    p = Product("A", "Apple", 2.0)
    cat.add_product(p)

    cart = Cart(cat)
    cart.add_item("A", 3)
    assert cart.get_total() == 6.0