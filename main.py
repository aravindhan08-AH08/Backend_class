from fastapi import FastAPI
from db.database import Base, engine
# routers -> foods router import
# step-1
from routers.foods import food_router
from routers.restaurant import restaurant_router
from routers.orders import orders_router
from routers.user import user_router
from routers.order_item import order_items_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
# step -2
# decorator function
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(food_router)
app.include_router(restaurant_router)
app.include_router(orders_router)
app.include_router(user_router)
app.include_router(order_items_router)