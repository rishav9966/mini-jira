from fastapi import HTTPException, status
from app.models.issue import Issue
from app.models.project import Project
from app.models.user import User

class IssueRepository:
    def __init__(self, db):
        self.db = db

    def create_issue(self, issue_data):
        project = self.db.query(Project).filter(Project.id == issue_data.project_id).first()
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Project with id {issue_data.project_id} does not exist."
            )
        owner = self.db.query(User).filter(User.id == issue_data.created_by).first()
        if not owner:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {issue_data.created_by} does not exist."
            )
        if issue_data.assigned_to is not None:
            assignee = self.db.query(User).filter(User.id == issue_data.assigned_to).first()
            if not assignee:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User with id {issue_data.assigned_to} does not exist."
                )
        issue = Issue(**issue_data.model_dump())
        self.db.add(issue)
        self.db.flush()
        return issue

    def get_issue(self, issue_id):
        issue = self.db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Issue with id {issue_id} does not exist."
            )
        return issue

    def update_issue_status(self, issue_id, status):
        issue = self.db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Issue with id {issue_id} does not exist."
            )
        issue.status = status
        self.db.add(issue)
        return issue

    def assign_issue(self, issue_id, assign_to):
        user = self.db.query(User).filter(User.id == assign_to).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {assign_to} does not exist.",
            )
        issue = self.db.query(Issue).filter(Issue.id == issue_id).first()
        if not issue:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Issue with id {issue_id} does not exist."
            )
        issue.assigned_to = assign_to
        self.db.add(issue)
        return issue

    def get_issues_by_assignee(self, assignee_id):
        return self.db.query(Issue).filter(Issue.assigned_to == assignee_id).all()