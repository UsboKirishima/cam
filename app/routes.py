from flask import Blueprint, render_template, Response, url_for
from .camera import get_frames

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('camera.html')

@main.route('/video_feed')
def video_feed():
    return Response(get_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
