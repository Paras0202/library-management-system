from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class MemberCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    joined_date: date

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
