from enum import auto

from api.database   import ApiBase
from sqlalchemy     import Text, String
from sqlalchemy.orm import Mapped, mapped_column


class User(ApiBase):
    __tablename__ = "users"

    id        : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    email     : Mapped[str] = mapped_column(String(255))
    name      : Mapped[str] = mapped_column(Text(50))
    pass_hash : Mapped[str] = mapped_column(String(255))
