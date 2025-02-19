from app.routes import app
from app.sockets import socketio

if __name__ == "__main__":
    socketio.run(app, debug=True)

