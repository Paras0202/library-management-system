from pydantic import BaseModel, EmailStr
from datetime import date

class MemberResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    joined_date: date

    class Config:
        from_attributes = True  # Enables ORM support
