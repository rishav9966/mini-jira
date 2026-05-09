from fastapi import APIRouter, Depends

from app.deps import get_user_service
from app.schema.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, user_service=Depends(get_user_service)):
    return user_service.create_user(payload=user)
