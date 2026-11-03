from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = "sqlite:///./pilfer.db"

engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}
        )

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    ...

def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as db:
        yield db
