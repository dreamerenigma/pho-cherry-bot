import pytest
from backend.models import MenuItem

def test_menu_item_creation():
    item = MenuItem(name="Burger", price=5.99, description="Juicy beef burger")
    assert item.name == "Burger"
    assert item.price == 5.99
    assert item.description == "Juicy beef burger"

def test_menu_list_structure():
    menu = [
        MenuItem(name="Burger", price=5.99, description="Juicy beef burger"),
        MenuItem(name="Fries", price=2.99, description="Crispy fries"),
    ]
    assert all(hasattr(i, "name") and hasattr(i, "price") for i in menu)
