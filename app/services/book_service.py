from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.domain.book import Book
from app.schemas.v1.requests.book import BookCreate, BookUpdate
from fastapi import HTTPException

class BookService:
    @staticmethod
    async def get_books(db: AsyncSession):
        result = await db.execute(select(Book))
        return result.scalars().all()

    @staticmethod
    async def get_book(book_id: int, db: AsyncSession):
        result = await db.execute(select(Book).where(Book.id == book_id))
        book = result.scalar_one_or_none()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @staticmethod
    async def create_book(book_data: BookCreate, db: AsyncSession):
        book = Book(**book_data.dict())
        db.add(book)
        await db.commit()
        await db.refresh(book)
        return book

    @staticmethod
    async def update_book(book_id: int, update_data: BookUpdate, db: AsyncSession):
        book = await BookService.get_book(book_id, db)
        for field, value in update_data.dict(exclude_unset=True).items():
            setattr(book, field, value)
        await db.commit()
        await db.refresh(book)
        return book

    @staticmethod
    async def delete_book(book_id: int, db: AsyncSession):
        book = await BookService.get_book(book_id, db)
        await db.delete(book)
        await db.commit()
        return {"message": "Book deleted successfully"}
