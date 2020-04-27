from dataclasses import dataclass


@dataclass
class FoodItem:
    food_item_id: int
    food_item_name: str
    description: str
    price: int
    food_category_id: int
    discount: int
