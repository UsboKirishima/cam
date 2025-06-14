import requests
import socket
import psutil
from datetime import datetime

def get_public_ip() -> str:
    try:
        response = requests.get('https://jsonip.com/')
        if response.status_code == 200:
            return response.json()['ip']
        else:
            return "unknown"
    except Exception:
        return "unknown"

def get_local_ip() -> str:
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception:
        return "unknown"

def get_lan_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        lan_ip = s.getsockname()[0]
        s.close()
        return lan_ip if lan_ip.startswith(('192.168.', '10.', '172.')) else get_local_ip()
    except Exception:
        return "unknown"

def get_ram_usage() -> str:
    mem = psutil.virtual_memory()
    return f"{mem.percent}%"

def get_cpu_usage() -> str:
    return f"{psutil.cpu_percent(interval=1)}%"

def get_server_uptime(start_time):
    uptime_seconds = (datetime.now() - start_time).total_seconds()
    
    if uptime_seconds < 60:
        return f"{int(uptime_seconds)} seconds"
    elif uptime_seconds < 3600:
        minutes = int(uptime_seconds // 60)
        return f"{minutes} minutes"
    elif uptime_seconds < 86400:
        hours = int(uptime_seconds // 3600)
        return f"{hours} hours"
    else:
        days = int(uptime_seconds // 86400)
        return f"{days} days"