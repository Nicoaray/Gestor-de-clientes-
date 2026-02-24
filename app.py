from flask import Flask
from config import Config
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # <-- ESTA LÍNEA ES CLAVE

    db.init_app(app)

    return app

app = create_app()