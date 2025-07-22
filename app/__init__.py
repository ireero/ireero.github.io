from flask import Flask
from .main import main as main_bp

def create_app(config_object='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(main_bp)
    return app
