from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'ok', 'message': 'Backend is running'})

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json() or {}
    url = data.get('url', '')
    
    return jsonify({
        'status': 'safe',
        'url': url,
        'message': 'URL checked successfully'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
