from flask import Flask
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the backend address from the environment variable or use a default value
backend_address = os.environ.get('BACKEND_ADDRESS', 'http://127.0.0.1:5000')

# Parse the backend address to get the host and port
if 'http' in backend_address:
    # If the address includes 'http', remove it
    backend_address = backend_address.split('://')[1]

host, port = backend_address.split(':')

@app.route('/')
def hello_world():
    return f'Hello, World! Backend is at: {backend_address}'

if __name__ == '__main__':
    app.run(host=host, port=int(port))
