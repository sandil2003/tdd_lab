import pytest
from src.catalog import Catalog, Product

def test_product_creation_validation():
    with pytest.raises(ValueError):
        Product(sku="SHIRT-01", name="T-Shirt", price=10.0)

def test_catalog_search_missing():
    catalog = Catalog()
    assert catalog.get_by_sku("MISSING") is None