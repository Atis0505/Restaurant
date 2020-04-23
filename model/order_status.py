from typing import List


class OrderStatus:
    def __init__(self, ordered_list):
        self.ordered_list: List = ordered_list

    def get_ordered_list(self) -> List[str]:
        return self.ordered_list

    def add_new_item(self, new_item):
        self.ordered_list.append(new_item)
