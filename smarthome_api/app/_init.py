from flask import Flask
from flask_socketio import SocketIO
from app.routes import register_routes

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    register_routes(app)
    socketio.init_app(app)
    return app

