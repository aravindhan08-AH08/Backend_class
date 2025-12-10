from pydantic import BaseModel

class UserSchema(BaseModel):
    user_name:str
    city:str
    contact:str
    email:str