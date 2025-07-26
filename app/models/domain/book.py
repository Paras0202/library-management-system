from sqlalchemy import Column, Integer, String, Enum
from app.models.domain.base import Base
import enum

class BookStatus(str, enum.Enum):
    available = "available"
    issued = "issued"
    lost = "lost"

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    status = Column(Enum(BookStatus), default=BookStatus.available)
