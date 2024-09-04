from flask import Flask
from .config import Config
from .models import db
from .routes import auth_bp, clients_bp, transactions_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(transactions_bp)

    return app
