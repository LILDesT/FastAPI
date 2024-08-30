from sqlalchemy import select
from fastapi import APIRouter
from FastAPI.database import async_session_maker
from FastAPI.bookings.models import Bookings
from FastAPI.bookings.dao import BookingDAO

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
    
)
@router.get("/bookings")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Bookings)  # SELECT * FROM bookings;
        result = await session.execute(query)
        bookings = result.mappings().all()  # Extract the results
        return bookings
    
@router.get("")
async def get_bookings2():
    return await BookingDAO.find_all()