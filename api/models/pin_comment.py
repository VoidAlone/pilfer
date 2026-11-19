from api.database import ApiBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MapperEvents, mapped_column, relationship


class PinComment(ApiBase):
    __tablename__ = "pin_comments"

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)
    pin_id  : Mapped[int] = mapped_column(ForeignKey("pins.id"), primary_key=True)
    user    : Mapped["User"] = relationship(back_populates="comments")
    pin     : Mapped["Pin"]  = relationship(back_populates="comments")

