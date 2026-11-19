from api.database   import ApiBase
from enum           import auto
from sqlalchemy     import Text, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(ApiBase):
    __tablename__ = "users"

    id        : Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    email     : Mapped[str] = mapped_column(String(255))
    name      : Mapped[str] = mapped_column(Text(50))
    pass_hash : Mapped[str] = mapped_column(String(255))
    comments  : Mapped[list["PinComment"]]  = relationship(back_populates="user")
    reactions : Mapped[list["PinReaction"]] = relationship(back_populates="user")

