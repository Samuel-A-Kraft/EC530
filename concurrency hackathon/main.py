from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from queue_manager import job_queue
from config import WORKER_COUNT
from worker_thread import start_threads

app = FastAPI()

class CountryRequest(BaseModel):
    country: str

start_threads(WORKER_COUNT)

@app.post("/covid")
def queue_country_job(request: CountryRequest):
    if job_queue.full():
        raise HTTPException(status_code=429, detail="Queue is full")
    job_queue.put(request.country.strip())
    return {"status": "queued", "country": request.country}