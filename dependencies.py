from db.database import SessionLocal

def connect_to_db():
    db = SessionLocal()
    try:
        print("Conected to DB")
        yield db
    finally:
        
        db.close()