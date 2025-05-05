from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from .db.db_connection import create_db_and_tables
from src.routers import

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Starting")
    create_db_and_tables()
    yield
    print("Server Stopped")


app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/api")

@app.get("/hello")
def hello():
    return {"Hello": "There"}

@app.post("/why")
def why():
    return {"Why": "not working!"}

# app.include_router(projects.router, prefix="/api")
