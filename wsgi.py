"""Production WSGI server configuration for Docker deployment."""

import os
from run import app

# Gunicorn configuration (for production use with docker)
workers = int(os.getenv("GUNICORN_WORKERS", 4))
worker_class = "sync"
bind = f"{os.getenv('FLASK_HOST', '0.0.0.0')}:{os.getenv('FLASK_PORT', 5000)}"
timeout = 30
keepalive = 2
