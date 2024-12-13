import socketio
import eventlet
import numpy as np
from flask import Flask
from keras.models import load_model
import base64
from io import BytesIO
from PIL import Image
import cv2

sio = socketio.Server()
app = Flask(__name__)
speed_limit = 10

# Image preprocessing
def img_preprocess(img):
    img = img[60:135, :, :]  # Crop image
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)  # Convert to YUV color space
    img = cv2.GaussianBlur(img, (3, 3), 0)  # Apply Gaussian Blur
    img = cv2.resize(img, (200, 66))  # Resize image
    img = img / 255.0  # Normalize image
    return img

# Handle telemetry data
@sio.on('telemetry')
def telemetry(sid, data):
    try:
        speed = float(data['speed'])
        image = Image.open(BytesIO(base64.b64decode(data['image'])))
        image = np.asarray(image)
        image = img_preprocess(image)
        image = np.array([image])
        
        steering_angle = float(model.predict(image))
        throttle = 1.0 - speed / speed_limit
        print('{} {} {}'.format(steering_angle, throttle, speed))
        
        send_control(steering_angle, throttle)
    except KeyError as e:
        print(f"Missing data: {e}")
    except Exception as e:
        print(f"Error processing telemetry data: {e}")

# Handle connect event
@sio.on('connect')
def connect(sid, environ):
    print('Connected')
    send_control(0, 0)

# Send control commands
def send_control(steering_angle, throttle):
    sio.emit('steer', data={
        'steering_angle': str(steering_angle),
        'throttle': str(throttle)
    })

if __name__ == '__main__':
    try:
        model = load_model('model/model.h5')
    except Exception as e:
        print(f"Error loading model: {e}")
        exit(1)
    
    app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)
