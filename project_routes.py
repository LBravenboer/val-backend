from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
import datetime

router = APIRouter()

class Project(BaseModel):
    id: int
    klantnaam: str
    uitslagorder: str
    deadline: datetime.date
    instructies: str
    materialen: Optional[str] = None
    prioriteit: int
    status: str = "In Progress"

projects_db = []

@router.post("/add_project/")
def add_project(project: Project):
    projects_db.append(project)
    return {"message": "Project toegevoegd", "data": project}

@router.get("/projects/")
def get_projects():
    return projects_db

@router.put("/update_project/{project_id}")
def update_project(project_id: int, status: str):
    for project in projects_db:
        if project.id == project_id:
            project.status = status
            return {"message": "Projectstatus bijgewerkt", "data": project}
    return {"error": "Project niet gevonden"}
