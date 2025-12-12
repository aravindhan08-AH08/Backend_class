from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from db.database import Base

class customers(Base):
    __tablename__="customers"
    id=Column(Integer,primary_key=True,index=True)
    user_name=Column(String)
    contact=Column(String)
    city=Column(String)
    email=Column(String)