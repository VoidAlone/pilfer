from pydantic import BaseModel, ConfigDict


class PinCreate(BaseModel):
    name: str
    path: str
    desc: str | None = None

class PinUpdate(BaseModel):
    name: str | None = None
    desc: str | None = None

class PinResponse(PinCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
