from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.database import get_db
from app.schemas.v1.requests.loan import LoanCreate, LoanUpdate
from app.schemas.v1.responses.loan import LoanResponse
from app.services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.get("/", response_model=List[LoanResponse])
async def get_loans(db: AsyncSession = Depends(get_db)):
    return await LoanService.get_loans(db)

@router.get("/{loan_id}", response_model=LoanResponse)
async def get_loan(loan_id: int, db: AsyncSession = Depends(get_db)):
    return await LoanService.get_loan(loan_id, db)

@router.post("/", response_model=LoanResponse, status_code=201)
async def create_loan(loan: LoanCreate, db: AsyncSession = Depends(get_db)):
    return await LoanService.create_loan(loan, db)

@router.put("/{loan_id}", response_model=LoanResponse)
async def update_loan(loan_id: int, loan: LoanUpdate, db: AsyncSession = Depends(get_db)):
    return await LoanService.update_loan(loan_id, loan, db)

@router.delete("/{loan_id}")
async def delete_loan(loan_id: int, db: AsyncSession = Depends(get_db)):
    return await LoanService.delete_loan(loan_id, db)
