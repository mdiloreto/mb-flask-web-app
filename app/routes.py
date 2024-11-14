from flask import Blueprint, jsonify, render_template
import os

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h1>Welcome to the Flask Web App!</h1><p>This is the homepage.</p>"

@main.route("/api")
def api():
    data = {"message": "Hello, API!", "items": ["item1", "item2", "item3"]}
    return jsonify(data)

@main.route("/environment")
def environment():
    environment = os.getenv("FLASK_ENV", "development")
    return f"<p>Current Environment: {environment}</p>"
