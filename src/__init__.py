from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from contextlib import asynccontextmanager

from .db.db_connection import create_db_and_tables
from .routers import users, projects


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Starting")
    create_db_and_tables()
    yield
    print("Server Stopped")

app = FastAPI(lifespan=lifespan)

app.include_router(users.router, prefix="/api")
app.include_router(projects.router, prefix="/api")

@app.get("/hello")
def hello():
    return {"Hello": "There"}
