from api.database   import ApiBase
from datetime       import datetime
from enum           import Enum
from sqlalchemy.orm import Mapped, mapped_column 
from sqlalchemy     import Enum as SqlEnum, DateTime, ForeignKey, Text, String, func


TIMESTAMP = DateTime(timezone=True)

class Visibility(str, Enum):
    PUBLIC="public"
    PRIVATE="private"

class Board(ApiBase):
    __tablename__ = "boards"

    id          : Mapped[int]        = mapped_column(primary_key=True, autoincrement=True)
    name        : Mapped[str]        = mapped_column(String(255))
    desc        : Mapped[str | None] = mapped_column(Text)
    created_by  : Mapped[int]        = mapped_column(ForeignKey("users.id"))
    created_on  : Mapped[datetime]   = mapped_column(TIMESTAMP, server_default=func.now())
    visibility  : Mapped[Visibility] = mapped_column(SqlEnum(Visibility))
