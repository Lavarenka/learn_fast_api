from fastapi import APIRouter
from users.schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def create_user(user: CreateUser):
    """
    CreateUser get from schemas

    """
    return crud.create_user(user_in=user)
