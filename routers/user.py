from fastapi import APIRouter,HTTPException,Depends
from models.user_model import Users
from schemas.user_schema import UserSchema
from dependencies import connect_to_db
from sqlalchemy.orm import Session

user_router=APIRouter(prefix="/user",tags=["User"])

@user_router.get("/")
def get_all_user(dbs:Session=Depends(connect_to_db)):
    users=dbs.query(Users).all()
    return users

@user_router.get("{id}")
def get_user_by_id(id:int,dbs:Session=Depends(connect_to_db)):
    user_num=dbs.query(Users).filter(Users.id==id).first()
    if not user_num:
        raise HTTPException(status_code=404,detail="user not found")
    return user_num

@user_router.post("/")
def post_user(new_user:UserSchema,dbs:Session=Depends(connect_to_db)):
    new_user=Users(
        user_name=new_user.user_name,
        city=new_user.city,
        contact=new_user.contact,
        email=new_user.email
    )
    dbs.add(new_user)
    dbs.commit()
    dbs.refresh(new_user)
    return {"message":"User added","data":new_user}

@user_router.put("/{id}")
def edit_user(id:int,user_update:UserSchema,dbs:Session=Depends(connect_to_db)):
    user_new=dbs.query(Users).filter(Users.id==id).first()
    if not user_new:
        raise HTTPException(status_code=404,details="User not found")
    user_new.user_name=user_update.user_name
    user_new.city=user_update.city
    user_new.contact=user_update.contact
    user_new.email=user_update.email
    dbs.commit()
    dbs.refresh(user_new)
    return {"message":"User not found","data":user_new}

@user_router.delete("/{id}")
def delete_user(id:int,dbs:Session=Depends(connect_to_db)):
    new_cus=dbs.query(Users).filter(Users.id==id).first()
    if not new_cus:
        raise HTTPException(status_code=404,details="User not found")
    dbs.delete(new_cus)
    dbs.commit()
    return {"message":"User deleted"}