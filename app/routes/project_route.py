from fastapi import APIRouter, Depends

from app.deps import get_project_service
from app.schema.project_schema import ProjectCreate, ProjectIssuesResponse, ProjectResponse

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/", response_model=ProjectResponse)
def create_project(
    project_data: ProjectCreate, project_service=Depends(get_project_service)
):
    return project_service.create_project(project_data)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, project_service=Depends(get_project_service)):
    return project_service.get_project(project_id=project_id)

@router.get("/owner/{owner_id}", response_model=list[ProjectResponse])
def get_project_by_owner(owner_id: int, project_service=Depends(get_project_service)):
    return project_service.get_projects_by_owner(owner_id=owner_id)


@router.get("/{project_id}/issues", response_model=list[ProjectIssuesResponse])
def get_issues_by_project(
    project_id: int, project_service=Depends(get_project_service)
):
    return project_service.get_issues_by_project(project_id=project_id)
