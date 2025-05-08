from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Device
from schemas import DeviceSchema
from database import SessionLocal

router = APIRouter(prefix="/devices", tags=["Devices"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=DeviceSchema)
def create_device(name: str, room_id: int, db: Session = Depends(get_db)):
    device = Device(name=name, room_id=room_id)
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

@router.get("/", response_model=list[DeviceSchema])
def list_devices(db: Session = Depends(get_db)):
    return db.query(Device).all()

@router.put("/{device_id}", response_model=DeviceSchema)
def toggle_device(device_id: int, status: str, db: Session = Depends(get_db)):
    device = db.query(Device).filter(Device.id == device_id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    device.status = status
    db.commit()
    db.refresh(device)
    return device
