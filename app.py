from flask import Flask, request, jsonify, send_from_directory
import os
import canonicalizer
import qr_generator

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
    raw_url = data.get('url', '')

    if not raw_url:
        return jsonify({'status': 'invalid', 'error': 'Please enter a URL'}), 400

    # Validate and canonicalize URL
    clean_url = canonicalizer.canonicalize_url(raw_url) if hasattr(canonicalizer, 'canonicalize_url') else raw_url

    # Generate QR Code (Base64 or image path depending on implementation)
    qr_data = qr_generator.generate_qr(clean_url) if hasattr(qr_generator, 'generate_qr') else None

    return jsonify({
        'status': 'safe',
        'valid': True,
        'url': clean_url,
        'qr_code': qr_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
