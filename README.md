# 📚 Library Management System

A FastAPI-based backend system to manage books, members, and loans.

## 🚀 Features

- Async PostgreSQL with SQLAlchemy 2.0
- Modular routers (Books, Members, Loans, Reports)
- Environment config via `.env`
- Swagger & Postman compatible

## 🔧 Setup

```bash
git clone https://github.com/Paras0202/library-management-system.git
cd library-management-system
python -m venv .venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```
