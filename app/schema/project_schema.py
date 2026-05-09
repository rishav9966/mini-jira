from pydantic import BaseModel, ConfigDict
from typing import Optional

from app.schema.issues_schema import IssueResponse

class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    owner_id: int

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

class ProjectIssuesResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int
    issues: list[IssueResponse]

    model_config = ConfigDict(from_attributes=True)