from app.repo.issue_repo import IssueRepository
from app.schema.issues_schema import IssueCreate, IssueResponse

class IssueService:
    def __init__(self, db):
        self.db = db
        self.issue_repo = IssueRepository(db)
        
    def create_issue(self, issue_data: IssueCreate):
        new_issue = self.issue_repo.create_issue(issue_data)
        self.db.commit()
        self.db.refresh(new_issue)
        return IssueResponse.model_validate(new_issue)
    
    def get_issue(self, issue_id: int):
        issue = self.issue_repo.get_issue(issue_id)
        return IssueResponse.model_validate(issue)
    
    def update_issue_status(self, issue_id: int, status):
        issue = self.issue_repo.update_issue_status(issue_id, status)
        self.db.commit()
        self.db.refresh(issue)
        return IssueResponse.model_validate(issue)
    
    def assign_issue(self, issue_id:int, assign_to:int):
        issue = self.issue_repo.assign_issue(issue_id, assign_to)
        self.db.commit()
        self.db.refresh(issue)
        return IssueResponse.model_validate(issue)
    
    def get_issues_by_assignee(self, assignee_id: int):
        issues = self.issue_repo.get_issues_by_assignee(assignee_id)
        return [IssueResponse.model_validate(issue) for issue in issues]