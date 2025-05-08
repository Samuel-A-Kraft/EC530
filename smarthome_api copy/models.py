from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class House(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    floors = relationship("Floor", back_populates="house")

class Floor(Base):
    __tablename__ = "floors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    house_id = Column(Integer, ForeignKey("houses.id"))
    house = relationship("House", back_populates="floors")
    rooms = relationship("Room", back_populates="floor")

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    floor_id = Column(Integer, ForeignKey("floors.id"))
    floor = relationship("Floor", back_populates="rooms")
    devices = relationship("Device", back_populates="room")

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String, default="off")
    room_id = Column(Integer, ForeignKey("rooms.id"))
    room = relationship("Room", back_populates="devices")
