from sqlalchemy import Column, Integer, String, Date
from app.models.domain.base import Base

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    joined_date = Column(Date, nullable=False)
