from dataclasses import dataclass


@dataclass
class FoodCategories:
    food_category_id: int
    food_category_name: str
    descrioption: str
    discount: int
