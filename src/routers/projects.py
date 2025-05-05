from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, select

from ..db.db_connection import get_db
from ..app.dtos import ProjectCreate, ProjectRead
from ..db.models import Project
from ..app.auth_decorators import auth_required, admin_required


router = APIRouter()


@router.get("/projects", response_model=list[ProjectRead])
@auth_required
def get_projects(request: Request, db: Session = Depends(get_db)):
    projects = db.exec(select(Project)).all()
    return projects

@router.post("/projects", response_model=ProjectRead)
@admin_required
def create_project(request: Request, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
