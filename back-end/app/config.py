import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'mysql+pymysql://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@mysql-db/{os.getenv("DB_NAME")}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-will-never-guess')
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
