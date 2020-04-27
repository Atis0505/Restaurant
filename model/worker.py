from dataclasses import dataclass
from datetime import date


@dataclass
class Worker:
    worker_id: int
    worker_name: str
    working_hours: int
    start_date: date
    end_date: date
