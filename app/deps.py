from fastapi import Depends
from app.db.deps import get_db
from app.services.project_svc import ProjectService
from app.services.user_svc import UserService
from app.services.issue_svc import IssueService

def get_project_service(db=Depends(get_db)):
    return ProjectService(db)

def get_user_service(db=Depends(get_db)):
    return UserService(db)

def get_issue_service(db=Depends(get_db)):
    return IssueService(db)