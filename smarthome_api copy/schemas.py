from pydantic import BaseModel
from typing import Optional

class HouseSchema(BaseModel):
    id: Optional[int]
    name: str

    class Config:
        orm_mode = True

class RoomSchema(BaseModel):
    id: Optional[int]
    name: str
    floor_id: Optional[int]

    class Config:
        orm_mode = True
class DeviceSchema(BaseModel):
    id: Optional[int]
    name: str
    status: str = "off"
    room_id: Optional[int]

    class Config:
        orm_mode = True
