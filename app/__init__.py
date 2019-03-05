from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config


db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['JWT_SECRET_KEY'] = 'SECRET'  # Change this!
    app.config['JWT_HEADER_TYPE'] = 'Token'  # Change this!
    app.conf = app.config
    db.init_app(app)

    return app


