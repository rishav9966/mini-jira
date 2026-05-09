from fastapi import APIRouter, Depends

from app.deps import get_project_service

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/")
def create_project(
    name: str, description: str, owner_id: int, project_service=Depends(get_project_service)
):
    return project_service.create_project(name=name, description=description, owner_id=owner_id)


@router.get("/{project_id}")
def get_project(project_id: int, project_service=Depends(get_project_service)):
    return project_service.get_project(project_id=project_id)

@router.get("/owner/{owner_id}")
def get_project_by_owner(owner_id: int, project_service=Depends(get_project_service)):
    return project_service.get_projects_by_owner(owner_id=owner_id)