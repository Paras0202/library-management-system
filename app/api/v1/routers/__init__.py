from .books import router as books_router
from .members import router as members_router
from .loans import router as loans_router
from .reports import router as reports_router

__all__ = [
    "books_router",
    "members_router",
    "loans_router",
    "reports_router"
]
