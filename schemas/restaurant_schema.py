from pydantic import BaseModel

class RestaurantCreate(BaseModel):
    restaurant_name:str
    location:str
    contact_person:str
    phone:str