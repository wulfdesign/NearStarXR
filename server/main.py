from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json

app = Flask(__name__, static_folder='../app', static_url_path='')
CORS(app) # Allow cross-origin requests

@app.route('/api/stars')
def get_stars():
    with open('stars.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)