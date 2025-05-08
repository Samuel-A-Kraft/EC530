from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import House
from database import SessionLocal

router = APIRouter(prefix="/houses", tags=["Houses"])

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_house(name: str, db: Session = Depends(get_db)):
    house = House(name=name)
    db.add(house)
    db.commit()
    db.refresh(house)
    return {"id": house.id, "name": house.name}

@router.get("/", response_model=list[dict])
def list_houses(db: Session = Depends(get_db)):
    houses = db.query(House).all()
    return [{"id": h.id, "name": h.name} for h in houses]

@router.get("/{house_id}", response_model=dict)
def get_house(house_id: int, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.id == house_id).first()
    if not house:
        raise HTTPException(status_code=404, detail="House not found")
    return {"id": house.id, "name": house.name}
