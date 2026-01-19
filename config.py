import os

# Flask
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-fitbrigade")

# SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///fitbrigade.db")

# Fix for Render: replace postgres:// with postgresql://
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False