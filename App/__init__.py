from flask import Flask, render_template, request
from .views import blue
import os

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/uploads'
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # register blueprints
    app.register_blueprint(blueprint = blue)

    return app