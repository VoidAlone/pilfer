from api.database     import ApiBase
from datetime         import datetime
from sqlalchemy       import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm   import Mapped, mapped_column


TIMESTAMP = DateTime(timezone=True)

class SavedPin(ApiBase):
    __tablename__ = "savedpins"

    id          : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pin_id      : Mapped[int] = mapped_column(ForeignKey("pins.id"))
    board_id    : Mapped[int] = mapped_column(ForeignKey("boards.id"))
    saved_by    : Mapped[int] = mapped_column(ForeignKey("users.id"))
    created_on  : Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

