from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Разрешает кросс-доменные запросы из браузера

OPENROUTER_API_KEY = 'ВАШ КЛЮЧ'
OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions'


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {OPENROUTER_API_KEY}',
            'HTTP-Referer': 'http://127.0.0.1:5000',
            'X-Title': 'AdultLife App'
        }

        response = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=30)

        if not response.ok:
            return jsonify({'error': response.text}), response.status_code

        return jsonify(response.json())

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
