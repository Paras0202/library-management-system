from pydantic import BaseModel
from datetime import date
from typing import Optional

class LoanResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    issue_date: date
    due_date: date
    return_date: Optional[date] = None
    returned: bool

    class Config:
        from_attributes = True  # Enables ORM -> Pydantic conversion
