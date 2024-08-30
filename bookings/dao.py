from FastAPI.database import async_session_maker
from sqlalchemy import select
from FastAPI.bookings.models import Bookings
from FastAPI.dao.base import BaseDAO

class BookingDAO(BaseDAO):
    model = Bookings