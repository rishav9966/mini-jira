from fastapi import HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.models.project import Project
from app.models.user import User


class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_project(self, name: str, description: str, owner_id: int):
        owner = self.db.query(User).filter(User.id == owner_id).first()
        if owner.role != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You don't have permission to create a project.") 
        if not owner:
            raise ValueError(f"User with id {owner_id} does not exist.")
        project = Project(name=name, description=description, owner_id=owner_id)
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
