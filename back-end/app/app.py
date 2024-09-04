from flask import Flask
from config import Config
from utils import db
from utils.db import init_db
from routes.auth import auth_bp
from routes.clients import clients_bp
from routes.transactions import transactions_bp

def create_app():
    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(transactions_bp)

    return app


app = create_app()

with app.app_context():
    init_db()  # No need to pass `app` again since the app context is already active

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
