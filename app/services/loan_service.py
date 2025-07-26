from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.models.domain.loan import Loan
from app.models.domain.book import Book, BookStatus
from app.schemas.v1.requests.loan import LoanCreate, LoanUpdate

class LoanService:
    @staticmethod
    async def get_loans(db: AsyncSession):
        result = await db.execute(select(Loan))
        return result.scalars().all()

    @staticmethod
    async def get_loan(loan_id: int, db: AsyncSession):
        result = await db.execute(select(Loan).where(Loan.id == loan_id))
        loan = result.scalar_one_or_none()
        if not loan:
            raise HTTPException(status_code=404, detail="Loan not found")
        return loan

    @staticmethod
    async def create_loan(loan_data: LoanCreate, db: AsyncSession):
        # Check if book is available
        result = await db.execute(select(Book).where(Book.id == loan_data.book_id))
        book = result.scalar_one_or_none()
        if not book or book.status != BookStatus.available:
            raise HTTPException(status_code=400, detail="Book is not available for loan")

        # Mark book as issued
        book.status = BookStatus.issued

        loan = Loan(**loan_data.dict())
        db.add(loan)
        await db.commit()
        await db.refresh(loan)
        return loan

    @staticmethod
    async def update_loan(loan_id: int, update_data: LoanUpdate, db: AsyncSession):
        loan = await LoanService.get_loan(loan_id, db)

        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(loan, field, value)

        # If returned, mark the book as available again
        if update_data.returned is True:
            result = await db.execute(select(Book).where(Book.id == loan.book_id))
            book = result.scalar_one_or_none()
            if book:
                book.status = BookStatus.available

        await db.commit()
        await db.refresh(loan)
        return loan

    @staticmethod
    async def delete_loan(loan_id: int, db: AsyncSession):
        loan = await LoanService.get_loan(loan_id, db)
        await db.delete(loan)
        await db.commit()
        return {"message": "Loan deleted successfully"}
