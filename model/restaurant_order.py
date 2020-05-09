from dataclasses import dataclass


@dataclass
class RestaurantOrder:
    order_id: int
    order_name: str
    time_stamp: str
    price: int
    making: int
    served: int
    paid: int
