from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Room
from schemas import RoomSchema
from database import SessionLocal

router = APIRouter(prefix="/rooms", tags=["Rooms"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RoomSchema)
def create_room(name: str, floor_id: int, db: Session = Depends(get_db)):
    room = Room(name=name, floor_id=floor_id)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

@router.get("/", response_model=list[RoomSchema])
def list_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()
