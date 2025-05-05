from sqlmodel import SQLModel, create_engine, Session
from .models import User, Project
import os

DATABASE_URL = os.environ.get("DATABASE_URI")

engine = create_engine(DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database connected")
