from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db.db_connection import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Starting")
    create_db_and_tables()
    yield
    print("Server Stopped")


app = FastAPI(lifespan=lifespan)

@app.get("/hello")
def hello():
    return {"Hello": "There"}
