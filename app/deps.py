from fastapi import Depends
from app.db.deps import get_db
from app.services.projects import ProjectService
from app.services.users import UserService

def get_project_service(db=Depends(get_db)):
    return ProjectService(db)

def get_user_service(db=Depends(get_db)):
    return UserService(db)