from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum

from app.db.base import Base

class IssueStatus(str, Enum):
    OPEN = "open"
    BLOCKED = "blocked"
    IN_PROGRESS = "in_progress"
    DEV_COMPLETED = "dev_completed"
    CLOSED = "closed"


class Issue(Base):
    __tablename__ = "issues"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(String, default=IssueStatus.OPEN.value)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    project = relationship("Project", back_populates="issues")
    creator = relationship("User", foreign_keys=[created_by], back_populates="created_issues")
    assignee = relationship("User", foreign_keys=[assigned_to], back_populates="assigned_issues")
    
    def __repr__(self):
        return f"<Issue(id={self.id}, title='{self.title}', description='{self.description}', status='{self.status}', project_id={self.project_id}, created_by={self.created_by}, assigned_to={self.assigned_to})>"
