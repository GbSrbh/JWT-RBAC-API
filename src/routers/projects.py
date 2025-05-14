from fastapi import APIRouter, Depends, Request
from sqlmodel import Session, select

from ..db.db_connection import get_db
from ..dtos import ProjectCreate, ProjectRead, UpdateProject
from ..db.models import Project
from ..handlers.auth_decorators import auth_required, admin_required


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

@router.put("/update-project/{project_id}", response_model=ProjectRead)
@admin_required
def update_project(request: Request, update_project: ProjectCreate, project_id: int, db: Session = Depends(get_db)):
    curr_project = db.exec(select(Project).where(Project.id==project_id)).first()

    update_data = update_project.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(curr_project, key, value)

    db.add(curr_project)
    db.commit()
    db.refresh(curr_project)
    return curr_project
