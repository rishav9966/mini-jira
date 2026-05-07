from fastapi import APIRouter, Depends
from app.db.deps import get_db
from app.models.user import User
from app.models.project import Project

router = APIRouter(prefix="/projects", tags=["projects"])


@router.post("/")
def create_project(name: str, description: str, owner_id: int, db=Depends(get_db)):
    owner = db.query(User).filter(User.id == owner_id).first()
    if not owner:
        raise ValueError("Owner not found")
    project = Project(name=name, description=description, owner_id=owner_id)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project