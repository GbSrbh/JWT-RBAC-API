from sqlmodel import SQLModel, create_engine, Session
from .models import User, Project

DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"

engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database connected")
