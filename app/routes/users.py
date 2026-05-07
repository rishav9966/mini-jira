from fastapi import APIRouter, Depends

from app.models.user import User
from app.db.deps import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def create_user(username:str, email:str, db=Depends(get_db)):
    user = User(username=username, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
