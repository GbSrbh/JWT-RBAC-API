from sqlmodel import SQLModel, Field
from ..app.dtos import Role

class UserBase(SQLModel):
    username: str = Field(index=True, unique=True)
    role: Role

class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str

class ProjectBase(SQLModel):
    name: str
    description: str

class Project(ProjectBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
