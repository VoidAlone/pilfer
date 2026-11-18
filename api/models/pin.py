from typing import List

from api.database   import ApiBase
from pin_reaction   import PinReaction
from pin_comment import PinComment
from sqlalchemy     import ARRAY, ForeignKey, String, Text, table
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Pin(ApiBase):
    __tablename__ = "pins"

    id  :       Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc:       Mapped[str | None] = mapped_column(Text) 
    name:       Mapped[str] = mapped_column(String(255))
    path:       Mapped[str] = mapped_column(String(1024))
    user:       Mapped[int] = mapped_column(ForeignKey="user.id")
    comments: Mapped[list["PinComment"]] = relationship(
            back_populates="pin"
            )
    reactions:  Mapped[list["PinReaction"]] = relationship(
            back_populates="pin"
            )
