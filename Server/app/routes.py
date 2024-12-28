from flask import render_template, current_app
from app import socketio
from .camera import generate_frames

def init_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('start_stream')
    def start_stream():
        for frame in generate_frames():
            socketio.emit('video_frame', frame)

# Call this function in __init__.py after creating the app
# init_routes(current_app)