from fastapi import FastAPI

from database import Base, engine
from models.pin import Pin
from routes import pin

app = FastAPI(title="KeePin")

# Temporary until we configure Alembic
Base.metadata.create_all(bind=engine)

app.include_router(pin.router)
