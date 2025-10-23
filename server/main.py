from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
from dotenv import load_dotenv
import os

# This line loads the variables from your .env file
load_dotenv()

# We point the static folder to the 'app' directory
app = Flask(__name__, static_folder='../app', static_url_path='')
CORS(app)

@app.route('/api/stars')
def get_stars():
    try:
        # --- This is the robust way to find the file ---
        # Get the absolute path of the directory where this script (main.py) lives
        script_dir = os.path.dirname(os.path.realpath(__file__))
        # Join that path with the filename
        json_path = os.path.join(script_dir, 'stars.json')
        
        with open(json_path) as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        # If anything goes wrong, print the error to the console and return a 500
        print(f"Error in get_stars: {e}")
        return str(e), 500

@app.route('/')
def index():
    # Serves the index.html from the 'app' folder
    return app.send_static_file('index.html')