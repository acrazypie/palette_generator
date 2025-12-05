#!/bin/bash
set -e

echo "Starting Palette Generator..."

# Run migrations or setup if needed (placeholder for future use)
# python manage.py db upgrade

# Start the Flask application
exec python run.py
