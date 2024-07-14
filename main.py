from fastapi import FastAPI, Query, Depends
from datetime import date
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class HotelsSearchArgs:
    def __init__(self,
        locations: str,
        date_from: date,
        date_to: date,
        has_spa: Optional[bool] = None,
        stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.location = locations
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars
class SHotel(BaseModel):
    adress:str
    name:str
    stars:int

list[SHotel]
@app.get("/hotels")
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
) -> list[SHotel]:


    hotels = [
        {
            "adress": "ул. Гагарина, Алтай",
            "name": "Super hotel",
            "stars": 5,
        }
    ]
    return hotels

class Sbooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: Sbooking):
    return