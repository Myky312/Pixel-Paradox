from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import json
from bson import ObjectId 

from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

# MongoDB configuration
mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/facerecognition')
client = MongoClient(mongo_uri)
db = client.get_default_database()


app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})
# Get the backend address from the environment variable or use a default value
backend_address = os.environ.get('BACKEND_ADDRESS', 'http://127.0.0.1:5000')

# Parse the backend address to get the host and port
if 'http' in backend_address:
    # If the address includes 'http', remove it
    backend_address = backend_address.split('://')[1]

host, port = backend_address.split(':')


def get_user_from_db(user_id):
    try:
        users_collection = db['users']
        # Retrieve all documents from the 'users' collection
        # Convert ObjectId to str for JSON serialization
        user = users_collection.find_one({'_id': ObjectId(user_id)})

        if user:
            return True
        else:
            return False
    except Exception as e:
        return {'error': str(e)}

@app.route('/')
def hello_world():
    return f'Hello, World! Backend is at: {backend_address}'


@app.route('/signup', methods=['POST'])
def signup():
    try:
        user_data = request.json
        user_id= user_data.get('_id')

        # Assume you have a list of existing emails and passwords
        if get_user_from_db(user_id):
            return "User already exists"
        else:
            faces_collection = db['users']
            result = faces_collection.insert_one(user_data)

            # Retrieve the inserted document's ID
            inserted_id = str(result.inserted_id)

            return {'message': 'Face added successfully', 'face_id': inserted_id}

    except Exception as e:
        return {'error': str(e)}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)