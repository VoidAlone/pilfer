from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Pin(Base):
    __tablename__ = "pins"

    id:     Mapped[int] = mapped_column(primary_key=True)
    name:   Mapped[str] = mapped_column(String(255))
    desc:   Mapped[str | None] = mapped_column(Text) 
    path:   Mapped[str] = mapped_column(String(1024))

