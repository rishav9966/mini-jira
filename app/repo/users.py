from sqlalchemy.orm import Session

from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, username:str, email:str):
        user = User(username=username, email=email)
        self.db.add(user)
        self.db.flush()  # Flush to get the ID assigned
        return user