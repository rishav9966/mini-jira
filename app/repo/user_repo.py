from sqlalchemy.orm import Session

from app.models.user import User
from app.schema.user_schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, user: UserCreate):
        db_user = User(username=user.username, email=user.email)
        self.db.add(db_user)
        self.db.flush()  # Flush to get the ID assigned
        return db_user