from sqlalchemy.orm import Mapped

from .base import Base


class Product(Base):
    # watch init file

    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
