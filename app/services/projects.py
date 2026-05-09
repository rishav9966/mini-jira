from app.models.project import Project
from app.repo.projects import ProjectRepository

class ProjectService:
    def __init__(self, db):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, name: str, description: str, owner_id: int):
        project = self.project_repo.create_project(name, description, owner_id)
        self.db.refresh(project)
        return project

    def get_project(self, project_id: int):
        return self.project_repo.get_project(project_id)

    def get_projects_by_owner(self, owner_id: int):
        return self.project_repo.get_projects_by_owner(owner_id)
