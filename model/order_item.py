from dataclasses import dataclass


@dataclass
class OrderItem:
    order_id: int
    order_name: str
    time_stamp: str
    worker_id: int
    price: int
    paid: int
