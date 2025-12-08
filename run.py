import os
from config import config
from app import create_app

# Load configuration based on FLASK_ENV
flask_env = os.getenv("FLASK_ENV", "development")
config_class = config.get(flask_env, config["default"])

# Create app with config
app = create_app()
app.config.from_object(config_class)

if __name__ == "__main__":
    host = os.getenv("FLASK_HOST", "0.0.0.0")
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host=host, port=port, debug=debug)
