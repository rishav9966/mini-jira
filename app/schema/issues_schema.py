from pydantic import BaseModel, ConfigDict
from typing import Optional

class IssueCreate(BaseModel):
    title:str
    description: Optional[str] = None
    project_id:int
    created_by:int
    assigned_to: Optional[int] = None

class IssueResponse(BaseModel):
    id: int
    title:str
    description: Optional[str] = None
    status: str
    project_id:int
    created_by:int
    assigned_to: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)