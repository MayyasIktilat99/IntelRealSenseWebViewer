from flask import Flask
from flask_socketio import SocketIO
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def create_app():
    app.config.from_object('config.Config')

    socketio.init_app(app)

    with app.app_context():
        from app import routes
        from .routes import init_routes
        init_routes(app)

    return app
