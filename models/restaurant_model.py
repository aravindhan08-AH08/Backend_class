from sqlalchemy import Column,Integer,String
from db.database import Base

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer,primary_key = True, index=True)
    restaurant_name = Column(String)
    location = Column(String)
    contact_person = Column(String)
    phone = Column(String)