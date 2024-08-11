from sqlalchemy import JSON, Column, Integer, String
from FASTAPI.database import Base # type: ignore

class Hotels(Base):
    __tablename__ = "hotels"
    
    id = Column(Integer, primary_key= True)
    name = Column(String, nullable = False)
    location = Column(String, nullable = False)
    services  = Column(JSON, nullable = False)
    room_quatity  = Column(Integer, nullable = False)
    image_id = Column(Integer, nullable = False)