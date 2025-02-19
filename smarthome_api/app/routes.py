from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
import unittest

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def response(success, data=None, message=None):
    return jsonify({"success": success, "data": data, "message": message})

# CRUD API Endpoints

# Users
@app.post("/users")
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return response(False, message="Missing required fields"), 400
    return response(True, {"id": 1, "name": data["name"], "email": data["email"]})

@app.get("/users/<int:user_id>")
def get_user(user_id):
    return response(True, {"id": user_id, "name": "Test User", "email": "test@example.com"})

@app.get("/users")
def list_users():
    return response(True, [{"id": 1, "name": "Test User", "email": "test@example.com"}])

@app.put("/users/<int:user_id>")
def update_user(user_id):
    data = request.json
    return response(True, {"id": user_id, "name": data.get("name", "Updated User"), "email": data.get("email", "updated@example.com")})

@app.delete("/users/<int:user_id>")
def delete_user(user_id):
    return response(True, message=f"User {user_id} deleted")

# Homes
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

@app.put("/homes/<int:home_id>")
def update_home(home_id):
    data = request.json
    return response(True, {"id": home_id, "address": data.get("address", "Updated Address")})

@app.delete("/homes/<int:home_id>")
def delete_home(home_id):
    return response(True, message=f"Home {home_id} deleted")

# Rooms
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

@app.put("/rooms/<int:room_id>")
def update_room(room_id):
    data = request.json
    return response(True, {"id": room_id, "name": data.get("name", "Updated Room")})

@app.delete("/rooms/<int:room_id>")
def delete_room(room_id):
    return response(True, message=f"Room {room_id} deleted")

# Devices
@app.get("/devices/status")
def get_devices_status():
    return response(True, {"devices": [{"id": 1, "type": "light", "status": "off", "room_id": 1}]})

@app.put("/devices/<int:device_id>/status")
def update_device_status(device_id):
    data = request.json
    if "status" not in data:
        return response(False, message="Missing status field"), 400
    updated_status = {"id": device_id, "status": data["status"]}
    socketio.emit("device_status_updated", updated_status)
    return response(True, updated_status)

# WebSocket Events for Real-time Updates
@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('request_status')
def send_status():
    emit("status_response", {"devices": [{"id": 1, "type": "light", "status": "off", "room_id": 1}]})

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

