from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import unittest

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def response(success, data=None, message=None):
    return jsonify({"success": success, "data": data, "message": message})

# Stub API Endpoints
@app.post("/users")
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return response(False, message="Missing required fields"), 400
    return response(True, {"id": 1, "name": data["name"], "email": data["email"]})

@app.post("/users/bulk")
def create_users_bulk():
    data = request.json
    if not isinstance(data, list) or not all("name" in user and "email" in user for user in data):
        return response(False, message="Invalid bulk user creation format"), 400
    return response(True, [{"id": i + 1, "name": user["name"], "email": user["email"]} for i, user in enumerate(data)])

@app.get("/users/<int:user_id>")
def get_user(user_id):
    return response(True, {"id": user_id, "name": "Test User", "email": "test@example.com"})

@app.get("/users")
def list_users():
    return response(True, [{"id": 1, "name": "Test User", "email": "test@example.com"}])

@app.post("/homes")
def create_home():
    data = request.json
    if not data or "address" not in data:
        return response(False, message="Missing required fields"), 400
    return response(True, {"id": 1, "address": data["address"]})

@app.get("/homes/<int:home_id>")
def get_home(home_id):
    return response(True, {"id": home_id, "address": "123 Main St"})

@app.get("/homes")
def list_homes():
    return response(True, [{"id": 1, "address": "123 Main St"}])

@app.post("/rooms")
def create_room():
    data = request.json
    if not data or "home_id" not in data or "name" not in data:
        return response(False, message="Missing required fields"), 400
    return response(True, {"id": 1, "home_id": data["home_id"], "name": data["name"]})

@app.get("/rooms/<int:room_id>")
def get_room(room_id):
    return response(True, {"id": room_id, "name": "Living Room", "home_id": 1})

@app.get("/rooms")
def list_rooms():
    return response(True, [{"id": 1, "name": "Living Room", "home_id": 1}])

@app.post("/devices")
def create_device():
    data = request.json
    if "type" not in data or "status" not in data or "room_id" not in data:
        return response(False, message="Missing required fields"), 400
    new_device = {"id": 1, "type": data["type"], "status": data["status"], "room_id": data["room_id"]}
    socketio.emit("device_created", new_device)
    return response(True, new_device)

@app.patch("/devices/<int:device_id>")
def update_device(device_id):
    data = request.json
    if "status" not in data:
        return response(False, message="Missing required status field"), 400
    updated_device = {"id": device_id, "type": "light", "status": data["status"]}
    socketio.emit("device_updated", updated_device)
    return response(True, updated_device)

@app.delete("/devices/<int:device_id>")
def delete_device(device_id):
    socketio.emit("device_deleted", {"device_id": device_id})
    return response(True, message=f"Device {device_id} deleted")

@app.get("/devices")
def list_devices():
    return response(True, [{"id": 1, "type": "light", "status": "off", "room_id": 1}])

# WebSocket Events
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('request_status')
def send_status():
    emit("status_response", {"devices": [{"id": 1, "type": "light", "status": "off", "room_id": 1}]})

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

# Unit Tests 
class TestSmartHomeAPI(unittest.TestCase):
    def test_create_user(self):
        self.assertEqual(response(True, {"id": 1, "name": "Test User", "email": "test@example.com"})[1], 200)
    
    def test_create_users_bulk(self):
        self.assertEqual(response(True, [{"id": 1, "name": "User1", "email": "user1@example.com"}])[1], 200)
    
    def test_create_home(self):
        self.assertEqual(response(True, {"id": 1, "address": "123 Main St"})[1], 200)
    
    def test_create_room(self):
        self.assertEqual(response(True, {"id": 1, "home_id": 1, "name": "Living Room"})[1], 200)
    
    def test_create_device(self):
        self.assertEqual(response(True, {"id": 1, "type": "light", "status": "off", "room_id": 1})[1], 200)

if __name__ == "__main__":
    unittest.main()

# GitHub Actions Workflow
"""
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install flask flask-socketio pytest
      - name: Run Tests
        run: python -m unittest discover
"""
