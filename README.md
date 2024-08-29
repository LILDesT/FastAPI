# FastAPI Project

A FastAPI-based application for user, booking, and hotel management. This project uses SQLAlchemy ORM, Alembic for migrations, and async PostgreSQL.

## Installation

```bash
git clone https://github.com/LILDesT/FastAPI.git
cd FastAPI
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

Usage
Run the application:

```bash
uvicorn main:app --reload
Visit http://127.0.0.1:8000 to access the API.

