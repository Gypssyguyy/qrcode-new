from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    if os.path.exists('public/index.html'):
        return send_from_directory('public', 'index.html')
    return "Flask app is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
