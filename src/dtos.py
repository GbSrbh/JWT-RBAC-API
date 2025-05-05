from typing import Union
from pydantic import BaseModel

class SignupRequest(BaseModel):
    username: str
    password: str
    role: str

class SignupResponse(BaseModel):
    username: str
    role: str

class LoginRequest(BaseModel):
    username: str
    password: str

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
