from pydantic import BaseModel
from enum import Enum
from typing import Optional

class BookStatus(str, Enum):
    available = "available"
    issued = "issued"
    lost = "lost"

class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str
    status: BookStatus = BookStatus.available

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    status: Optional[BookStatus] = None
