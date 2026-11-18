from typing import List

from api.database   import ApiBase
from sqlalchemy     import ARRAY, ForeignKey, String, Text, table
from sqlalchemy.orm import Mapped, mapped_column


class Pin(ApiBase):
    __tablename__ = "pins"

    id  :   Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc:   Mapped[str | None] = mapped_column(Text) 
    name:   Mapped[str] = mapped_column(String(255))
    path:   Mapped[str] = mapped_column(String(1024))
    user:   Mapped[int] = mapped_column(ForeignKey="user.id")
