from dataclasses import dataclass


@dataclass
class DrinkItem:
    drink_item_id: int
    drink_item_name: str
    description: str
    price: int
    category_id: int
    discount: int
