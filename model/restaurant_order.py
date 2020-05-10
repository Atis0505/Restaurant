from dataclasses import dataclass


@dataclass
class RestaurantOrder:
    restaurant_order_id: int
    start_time: str
    end_time: str
    price: int
    making: int
    served: int
    paid: int
