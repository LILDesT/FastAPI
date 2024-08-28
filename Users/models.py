from sqlalchemy import JSON, Column, Integer, String, Date, Computed
from FastAPI.database import Base 
from sqlalchemy import ForeignKey


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable = False)
    hashed_password = Column(String, nullable = False)