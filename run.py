from app import create_app

app = create_app()

if __name__ == '__main__':
    app.secret_key = 'supersecret'
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)