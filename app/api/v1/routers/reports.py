from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date

from app.config.database import get_db
from app.models.domain.loan import Loan
from app.schemas.v1.responses.loan import LoanResponse

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/overdue-loans", response_model=list[LoanResponse])
async def get_overdue_loans(db: AsyncSession = Depends(get_db)):
    today = date.today()
    result = await db.execute(
        select(Loan).where(Loan.due_date < today, Loan.returned == False)
    )
    return result.scalars().all()
