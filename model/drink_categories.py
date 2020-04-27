from dataclasses import dataclass


@dataclass
class DrinkCategories:
    drink_category_id: int
    drink_category_name: str
    description: str
    price: int
    alcohol_content: bool
    discount: int
