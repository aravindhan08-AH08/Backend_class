from fastapi import FastAPI
from db.database import Base, engine
# router -> foods router import
# step 1
from routers.foods import food_router
from routers import restaurant

from routers.user import user_router
Base.metadata.create_all(bind=engine)
app = FastAPI()


# decorator function
@app.get("/")
def read_root():
    return {"Hello":"World"}


#step 2
app.include_router(food_router)
# Add Restaurant this step important
app.include_router(restaurant.router)
# Add User In show swager ui
app.include_router(user_router)