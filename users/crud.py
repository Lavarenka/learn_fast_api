from users.chemas import CreateUser

def create_user(user_in: CreateUser) -> dict:

    user = user_in.model_dump()
    return {
        'success': True,
        'user': user,
    }


