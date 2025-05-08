import redis
import threading
import json

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def publish_message(topic: str, sender: str, content: str):
    message = {
        "topic": topic,
        "from": sender,
        "content": content
    }
    r.publish(topic, json.dumps(message))

def subscribe_to_topic(topic: str, callback):
    pubsub = r.pubsub()
    pubsub.subscribe(topic)
    
    def listen():
        for msg in pubsub.listen():
            if msg['type'] == 'message':
                payload = json.loads(msg['data'].decode())
                callback(payload)
    
    thread = threading.Thread(target=listen, daemon=True)
    thread.start()
