from FastAPI.database import async_session_maker
from sqlalchemy import select
from FastAPI.bookings.models import Bookings


class BaseDAO:
    model = None

    @classmethod #BookingDAO.find_all()
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)  # SELECT * FROM bookings;
            result = await session.execute(query)
            return result.mappings().all()