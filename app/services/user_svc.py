from app.db.deps import get_db
from app.repo.user_repo import UserRepository
from app.schema.user_schema import UserCreate, UserResponse

class UserService:
    def __init__(self, db):
        self.db = db
        self.user_repo = UserRepository(db)

    def create_user(self, user: UserCreate):
        new_user = self.user_repo.create_user(user)
        self.db.commit()
        self.db.refresh(new_user)
        return UserResponse.model_validate(new_user)
