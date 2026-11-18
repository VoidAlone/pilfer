from api.database import ApiBase
from user import User
from pin import Pin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, MapperEvents, mapped_column, relationship


class PinComment(ApiBase):
    __tablename__ = "pin_comments"

    user_id: Mapped[int] = mapped_column(
            ForeignKey="user.id",
            primary_key=True
            )

    pin_id: Mapped[int] = mapped_column(
            ForeignKey="pin.id",
            primary_key=True
            )

    user: Mapped["User"] = relationship(
            back_populates="comments"
            )

    pin: Mapped["Pin"] = relationship(
            back_populates="comments"
            )
