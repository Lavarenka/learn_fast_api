from users.schemas import CreateUser


def create_user(user_in: CreateUser) -> dict:
    """
    CreateUser get from schemas
    """
    user = user_in.model_dump()
    return {
        'success': True,
        'user': user,
    }
