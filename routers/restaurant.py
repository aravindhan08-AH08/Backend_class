from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.restaurant_model import Restaurant
from schemas.restaurant_schema import RestaurantCreate
router=APIRouter(
    prefix="/restaurant",
    tags=["Restaurant"]
)
@router.get("/")
def get_all_restaurant(dbs:Session=Depends(connect_to_db)):
    restaurant=dbs.query(Restaurant).all()
    return restaurant

@router.get("/{id}")
def get_restaurant_by_id(id:int,dbs:Session=Depends(connect_to_db)):
    restaurants=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not restaurants:
        raise HTTPException(status_code=404,details="Restaurant not found")
    return restaurants


@router.post ("/")
def create_restaurant(rest:RestaurantCreate,db:Session=Depends(connect_to_db)):
    val=Restaurant(
        restaurant_name=rest.restaurant_name,
        location=rest.location,
        contact_person=rest.contact_person,
        phone=rest.phone
    )
    db.add(val)
    db.commit()
    db.refresh(val)
    return val


@router.put("/{id}")
def edit_restaurant(id:int,res_update:RestaurantCreate,dbs:Session=Depends(connect_to_db)):
    res_new=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not res_new:
        raise HTTPException(status_code=404,details="Restaurant not found")
    res_new.restaurant_name=res_new.restaurant_name
    res_new.location=res_new.location
    res_new.contact_person=res_new.contact_person
    res_new.phone=res_new.phone
    dbs.commit()
    dbs.refresh(res_new)
    return {"message":"Restaurant update","data":res_new}

@router.delete("/{id}")
def delete_res(id:int,dbs:Session=Depends(connect_to_db)):
    res=dbs.query(Restaurant).filter(Restaurant.id==id).first()
    if not res:
        raise HTTPException(status_code=404,details="Restaurant not found")
    dbs.delete(res)
    dbs.commit()
    return {"message":"Restaurant deleted"}