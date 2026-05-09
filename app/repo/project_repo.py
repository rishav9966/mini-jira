from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.models.project import Project
from app.models.user import User

from app.schema.project_schema import ProjectCreate


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, project_data: ProjectCreate):
        owner = self.db.query(User).filter(User.id == project_data.owner_id).first()
        if not owner:
            raise ValueError(f"User with id {project_data.owner_id} does not exist.")
        if owner.role != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to create a project.")         
        project = Project(name=project_data.name, description=project_data.description, owner_id=project_data.owner_id)
        self.db.add(project)
        self.db.flush()
        return project

    def get_project(self, project_id: int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .options(joinedload(Project.owner))
            .first()
        )

    def get_projects_by_owner(self, owner_id: int):
        return (
            self.db.query(Project)
            .filter(Project.owner_id == owner_id)
            .all()
        )
    
    def get_issues_by_project(self, project_id: int):
        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .options(joinedload(Project.issues))
            .all()
        )
