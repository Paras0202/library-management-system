from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.config.database import get_db
from app.schemas.v1.requests.book import BookCreate, BookUpdate
from app.schemas.v1.responses.book import BookResponse
from app.services.book_service import BookService

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/", response_model=List[BookResponse])
async def get_books(db: AsyncSession = Depends(get_db)):
    return await BookService.get_books(db)

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: AsyncSession = Depends(get_db)):
    return await BookService.get_book(book_id, db)

@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(book: BookCreate, db: AsyncSession = Depends(get_db)):
    return await BookService.create_book(book, db)

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(book_id: int, book: BookUpdate, db: AsyncSession = Depends(get_db)):
    return await BookService.update_book(book_id, book, db)

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    return await BookService.delete_book(book_id, db)
