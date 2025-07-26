from fastapi import FastAPI
from app.db import engine
from app.models.domain.base import Base

from app.models.domain.book import Book
from app.models.domain.member import Member
from app.models.domain.loan import Loan
from app.api.v1.routers import books, members, loans, reports

app = FastAPI()

@app.on_event("startup")
async def startup():
    print("Creating tables...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tables created!")

@app.get("/")
async def root():
    return {"message": "Library Management System Running"}

app.include_router(books.router, prefix="/api/v1")
app.include_router(members.router, prefix="/api/v1")
app.include_router(loans.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")

