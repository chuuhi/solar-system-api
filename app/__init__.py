from flask import Flask
from .db import db, migrate
from .models.planet import Planet
from .routes.planet_routes import bp as planets_bp
import os
from dotenv import load_dotenv

load_dotenv()

def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(planets_bp)

    return app