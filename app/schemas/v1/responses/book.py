from pydantic import BaseModel
from enum import Enum

class BookStatus(str, Enum):
    available = "available"
    issued = "issued"
    lost = "lost"

class BookResponse(BaseModel):
    id: int
    isbn: str
    title: str
    author: str
    status: BookStatus

    class Config:
        from_attributes = True  # Enables ORM support
