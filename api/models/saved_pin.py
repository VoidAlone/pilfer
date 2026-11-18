from api.database     import ApiBase
from api.models.board import Board
from datetime         import datetime
from sqlalchemy       import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm   import Mapped, mapped_column


TIMESTAMP = DateTime(timezone=True)

class SavedPin(ApiBase):
    __tablename__ = "savedpins"

    id          : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pin         : Mapped[int] = mapped_column(ForeignKey="pin.id")
    board       : Mapped[int] = mapped_column(ForeignKey="board.id")
    created_by  : Mapped[int] = mapped_column(ForeignKey="user.id")
    created_on  : Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
