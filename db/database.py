from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import USERNAME, PASSWORD , HOSTNAME, DATABASE, PORT

print(USERNAME)
print(PASSWORD)
print(HOSTNAME)
print(DATABASE)
print(PORT)

DB_USERNAME = "postgres"
DB_PASSWORD = "AcademyRootPassword"
DB_HOSTNAME = "localhost"
DATABASE = "food_api"
DB_PORT = "5432"

DB_URL = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DATABASE}"

#create engine
engine = create_engine(DB_URL)

#create session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#create your Base
Base = declarative_base()