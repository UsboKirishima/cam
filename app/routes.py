from flask import Blueprint, render_template, Response, url_for, request, session, redirect
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .camera import get_frames

main = Blueprint('main', __name__)

@main.route('/')
@login_required 
def index():
    if current_user.is_authenticated:
        return render_template('camera.html')
    return '<a href="/login">Login</a>'

@main.route('/video_feed')
@login_required
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')