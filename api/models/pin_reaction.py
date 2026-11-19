from api.database import ApiBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship



class PinReaction(ApiBase):
    __tablename__ = "pin_reactions"

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)
    pin_id  : Mapped[int] = mapped_column(ForeignKey("pins.id"),primary_key=True)
    user    : Mapped["User"] = relationship(back_populates="reactions")
    pin     : Mapped["Pin"] = relationship(back_populates="reactions")

