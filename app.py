from os import environ
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Create Flask app
app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'admin123')
app.config['DEBUG'] = environ.get('DEBUG') == 'True'
app.config['PORT'] = 5000

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL', 'postgresql://postgres:admin@localhost/sockets')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="*")

# Models
from models import Chat

# Routes
from routes import open_chat, new_message

if __name__ == '__main__':
    socketio.run(app, port=app.config['PORT'])