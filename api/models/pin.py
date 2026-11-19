from typing import TYPE_CHECKING

from api.database   import ApiBase
from sqlalchemy     import ForeignKey, String, Text 
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from pin_reaction   import PinReaction
    from pin_comment import PinComment

class Pin(ApiBase):
    __tablename__ = "pins"

    id      : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    desc    : Mapped[str | None] = mapped_column(Text) 
    name    : Mapped[str] = mapped_column(String(255))
    path    : Mapped[str] = mapped_column(String(1024))
    user    : Mapped[int] = mapped_column(ForeignKey("users.id"))
    comments: Mapped[list["PinComment"]] = relationship(back_populates="pin")
    reactions: Mapped[list["PinReaction"]] = relationship(back_populates="pin")

