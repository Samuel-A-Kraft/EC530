from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.sockets import deliver_message

app = FastAPI()

class MessagePayload(BaseModel):
    target_ip: str
    target_port: int
    content: str

@app.get("/")
def home():
    return {"status": "Peer API active"}

@app.post("/send")
def send_message(payload: MessagePayload):
    try:
        deliver_message(payload.target_ip, payload.target_port, payload.content)
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from app.pubsub import publish_message
from fastapi import BackgroundTasks

class PubSubPayload(BaseModel):
    topic: str
    sender: str
    content: str

@app.post("/publish")
def publish(pub: PubSubPayload):
    publish_message(pub.topic, pub.sender, pub.content)
    return {"status": f"Message published to topic '{pub.topic}'"}
