import pyrealsense2 as rs
import numpy as np
import cv2
import base64
from app import socketio

def generate_frames():
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    pipeline.start(config)

    try:
        while True:
            frames = pipeline.wait_for_frames()
            color_frame = frames.get_color_frame()
            color_image = np.asanyarray(color_frame.get_data())
            
            ret, buffer = cv2.imencode('.jpg', color_image)
            frame = base64.b64encode(buffer).decode('utf-8')
            yield frame
    finally:
        pipeline.stop()
