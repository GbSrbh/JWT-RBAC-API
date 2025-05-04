from typing import Union
from pydantic import BaseModel
from enum import Enum

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserRead(BaseModel):
    username: str
    role: str

class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

class ProjectRead(ProjectCreate):
    id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class Payload(BaseModel):
    username: Union[str, None] = None
    role: Union[str, None] = None

class Role(Enum):
    USER = "USER"
    ADMIN = "ADMIN"
