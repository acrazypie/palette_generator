from flask import Flask


def create_app(config_object=None):
    app = Flask(__name__)

    # Load config if provided
    if config_object:
        app.config.from_object(config_object)

    from .routes import main

    app.register_blueprint(main)

    return app
