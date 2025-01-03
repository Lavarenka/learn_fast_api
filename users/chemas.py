from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MaxLen, MinLen


class CreateUser(BaseModel):
    """
    email and login validation
    """
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr