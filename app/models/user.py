from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum

from app.db.base import Base

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MANAGER = "manager"


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String, default=Role.USER.value)
    projects = relationship("Project", back_populates="owner")
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"