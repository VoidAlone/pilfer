from pydantic import BaseModel, ConfigDict

class PinCreate(BaseModel):
    name: str
    desc: str | None = None
    path: str

class PinUpdate(BaseModel):
    name: str | None = None
    desc: str | None = None

class PinResponse(PinCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
