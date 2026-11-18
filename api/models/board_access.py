from api.database   import ApiBase
from enum           import Enum
from sqlalchemy     import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class BoardRole(str, Enum):
    VIEWER="viewer"
    EDITOR="editor"

class BoardAccess(ApiBase):
    __tablename__ = "board_access"

    board_id: Mapped[int] = mapped_column(ForeignKey("board.id"), primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey("user.id"),  primary_key=True)
    role    : Mapped[BoardRole]

    
