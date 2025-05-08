from fastapi import FastAPI
from routers import house, room, device
from database import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Home API")

app.include_router(house.router)
app.include_router(room.router)
app.include_router(device.router)
