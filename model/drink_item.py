class DrinkItem:
    def __init__(self, id, name, desc, price, cat_id, disc):
        self.drink_item_id: int = id
        self.drink_item_name: str = name
        self.drink_description: str = desc
        self.drink_price: int = price
        self.drink_category_id: int = cat_id
        self.drink_discount: int = disc

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return self.drink_item_name

    def __eq__(self, other):
        return (self.drink_item_name) == (other.drink_item_name)
