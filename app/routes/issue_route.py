from fastapi import APIRouter, Depends

from app.models.issue import IssueStatus
from app.schema.issues_schema import IssueCreate, IssueResponse
from app.deps import get_issue_service

router = APIRouter(prefix="/issues", tags=["issues"])


@router.post("/", response_model=IssueResponse)
def create_issue(issue_data: IssueCreate, issue_service=Depends(get_issue_service)):
    return issue_service.create_issue(issue_data)

@router.get("/{id}", response_model=IssueResponse)
def get_issue(id: int, issue_service=Depends(get_issue_service)):
    return issue_service.get_issue(id)

@router.get("/assignee/{assignee_id}", response_model=list[IssueResponse])
def get_issues_by_assignee(assignee_id:int, issue_service=Depends(get_issue_service)):
    return issue_service.get_issues_by_assignee(assignee_id)

@router.patch("/{id}/status", response_model=IssueResponse)
def update_issue_status(id: int, status: IssueStatus, issue_service=Depends(get_issue_service)):
    return issue_service.update_issue_status(id, status)

@router.patch("/{id}/assign", response_model=IssueResponse)
def assign_issue(id:int, assign_to: int, issue_service=Depends(get_issue_service)):
    return issue_service.assign_issue(id, assign_to)