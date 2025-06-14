from app import create_app
from config import Config

app = create_app()

if __name__ == '__main__':
    app.secret_key = Config.SECRET_KEY
    app.run(host=Config.HOST, port=Config.PORT, threaded=True, debug=Config.DEBUG)