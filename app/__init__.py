from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["ENVIRONMENT"] = "development"  # Default environment

    # Import and register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
