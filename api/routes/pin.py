from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models.pin import Pin
from schema.pin import PinCreate, PinUpdate, PinResponse

router = APIRouter(prefix="/pins", tags=["pins"])

@router.get("/", response_model=list[PinResponse])
def get_pins(db: Session = Depends(get_db)):
    return db.scalars(select(Pin)).all()

@router.get("/{pin_id:int}", response_model=PinResponse, status_code=201)
def get_pin(pin_id: int, db: Session = Depends(get_db)):
    pin = db.get(Pin, pin_id)
    if pin is None:
        return HTTPException(404, "Pin not found")

    return pin

@router.post("/", response_model=PinResponse, status_code=201)
def create_pin(data: PinCreate, db: Session = Depends(get_db)):
    pin = Pin(**data.model_dump())

    db.add(pin)
    db.commit()
    db.refresh(pin)

    return pin

@router.patch("/{pin_id: int}", response_model=PinResponse, status_code=200)
def update_pin(pin_id: int, data: PinUpdate, db: Session = Depends(get_db)):
    pin = db.get(Pin, pin_id);

    if pin is None:
        return HTTPException(404, "Pin not found")

    for key,value in data.model_dump(exclude_unset=True).items():
        setattr(pin, key, value)

    db.commit()
    db.refresh(pin)

    return pin

@router.delete("/{pin_id:int}", status_code=204)
def delete_pin(pin_id: int, db: Session = Depends(get_db)):
    pin = db.get(Pin, pin_id)

    if pin is None:
        return HTTPException(404, "Pin not found")

    db.delete(pin)
    db.commit()
