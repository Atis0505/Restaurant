class FoodItem:
    def __init__(self, id, name, desc, price, cat_id, disc):
        self.food_item_id: int = id
        self.food_item_name: str = name
        self.food_description: str = desc
        self.food_price: int = price
        self.food_category_id: int = cat_id
        self.food_discount: int = disc

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.food_item_name

    def __eq__(self, other):
        return (self.food_item_name) == (other.food_item_name)
