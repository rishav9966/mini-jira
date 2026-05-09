from app.models.project import Project
from app.repo.project_repo import ProjectRepository
from app.schema.project_schema import ProjectCreate, ProjectResponse


class ProjectService:
    def __init__(self, db):
        self.db = db
        self.project_repo = ProjectRepository(db)

    def create_project(self, project_data: ProjectCreate):
        project = self.project_repo.create_project(project_data)
        self.db.commit()
        self.db.refresh(project)
        return ProjectResponse.model_validate(project)

    def get_project(self, project_id: int):
        return self.project_repo.get_project(project_id)

    def get_projects_by_owner(self, owner_id: int):
        return self.project_repo.get_projects_by_owner(owner_id)
