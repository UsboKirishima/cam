from flask import Blueprint, render_template, Response, url_for, request, session, redirect, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .camera import get_frames
from .host import *
from config import Config
from app import SERVER_START_TIME

main = Blueprint('main', __name__)

back_info = {
    'local_addr': get_local_ip(),
    'lan_ip': get_lan_ip(),
    'ip': get_public_ip(),
    'port': Config.PORT,
    'ram': get_ram_usage(),
    'cpu': get_cpu_usage(),
    'uptime': get_server_uptime(SERVER_START_TIME)
}

@main.route('/server-info', methods=['GET'])
def server_info():

    # update info each time page is requested
    back_info['ram'] = get_ram_usage()
    back_info['cpu'] = get_cpu_usage()
    back_info['uptime'] = get_server_uptime(SERVER_START_TIME)

    return jsonify(back_info)

@main.route('/')
@login_required 
def index():

    finfo = {
        'username': current_user.get_username()
    }

    if current_user.is_authenticated:
        return render_template('camera.html', info=back_info, finfo=finfo)
    return '<a href="/login">Login</a>'

@main.route('/video_feed')
@login_required
def video_feed():
    return Response(get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')