import os
import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_wtf.csrf import CSRFProtect

# Setup logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# Use environment variables for configuration
app.secret_key = os.getenv("SECRET_KEY", "replit-automarket-secret-key-2025")
app.config['WTF_CSRF_ENABLED'] = False

# Initialize CSRF protection  
# csrf = CSRFProtect(app)

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1) # needed for url_for to generate with https

# Configure the database using environment variables
# Priority: DATABASE_URL (for PostgreSQL/production) > SQLITE_PATH > default
database_url = os.getenv("DATABASE_URL")
if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
else:
    # Use SQLITE_PATH environment variable or default to instance/app.db
    sqlite_path = os.getenv("SQLITE_PATH", "instance/app.db")
    
    # Only create directory if it's a relative path (safer for deployment platforms)
    if not os.path.isabs(sqlite_path):
        db_dir = os.path.dirname(sqlite_path)
        if db_dir:
            try:
                os.makedirs(db_dir, exist_ok=True)
                logging.info(f"Created database directory: {db_dir}")
            except (PermissionError, OSError) as e:
                logging.warning(f"Could not create database directory {db_dir}: {e}")
                # Fall back to current directory
                sqlite_path = "app.db"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{sqlite_path}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure upload settings
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload directory exists (with error handling for deployment platforms)
try:
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
except (PermissionError, OSError) as e:
    logging.warning(f"Could not create upload directory: {e}")

# initialize the app with the extension, flask-sqlalchemy >= 3.0.x
db.init_app(app)

with app.app_context():
    # Make sure to import the models here or their tables won't be created
    import models  # noqa: F401

    db.create_all()

# Import routes after app creation
from routes import *

# Start the background scheduler for periodic tasks
try:
    from scheduler import start_scheduler
    start_scheduler()
    logging.info("Background scheduler started successfully")
except Exception as e:
    logging.error(f"Failed to start scheduler: {e}")