import os


class Config:
    """Base configuration"""

    # Flask Settings
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key-change-in-production"

    # Application Settings
    APP_NAME = "Palette Generator"
    APP_VERSION = "1.0.0"

    # Server Settings
    HOST = os.environ.get("FLASK_HOST", "0.0.0.0")
    PORT = int(os.environ.get("FLASK_PORT", 5000))

    # Security
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


class DevelopmentConfig(Config):
    """Development configuration"""

    DEBUG = True
    SECRET_KEY = "dev-secret-key"
    SESSION_COOKIE_SECURE = False  # Allow non-HTTPS in development
    LOG_LEVEL = "DEBUG"


class ProductionConfig(Config):
    """Production configuration"""

    DEBUG = False
    TESTING = False
    # In production, SECRET_KEY must be set via environment variable
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY environment variable is not set!")
    LOG_LEVEL = "WARNING"


class TestingConfig(Config):
    """Testing configuration"""

    TESTING = True
    DEBUG = True
    SECRET_KEY = "test-secret-key"


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
