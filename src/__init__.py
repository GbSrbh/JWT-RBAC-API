from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server starting")
    yield
    print("Server stopped")


app = FastAPI(lifespan=lifespan)

@app.get("/hello")
def hello():
    return {"Hello": "There"}
