import pytest
from unittest.mock import Mock
from src.catalog import Product, Catalog
from src.cart import Cart

def test_add_item_fails_when_inventory_insufficient():
    mock_inventory = Mock()
    mock_inventory.get_available.return_value = 5

    catalog = Catalog()
    catalog.add_product(Product("SKU-1", "Laptop", 1000.0))

    cart = Cart(catalog, inventory_service=mock_inventory)

    with pytest.raises(PermissionError, match="Insufficient inventory"):
        cart.add_item("SKU-1", 10)
        