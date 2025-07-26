from pydantic import BaseModel
from datetime import date
from typing import Optional

class LoanCreate(BaseModel):
    member_id: int
    book_id: int
    issue_date: date
    due_date: date
    return_date: Optional[date] = None
    returned: bool = False

class LoanUpdate(BaseModel):
    return_date: Optional[date] = None
    returned: Optional[bool] = None
