from app.db.deps import get_db
from app.repo.users import UserRepository

class UserService:
    def __init__(self, db):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, username: str, email: str):
        user = self.user_repo.create_user(username, email)
        self.db.commit()
        self.db.refresh(user)
        return user