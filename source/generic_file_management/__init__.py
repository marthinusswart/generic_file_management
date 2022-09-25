from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from generic_file_management.generic_file_management_api import create_api
from os import path
import os

db = SQLAlchemy()
DB_NAME = "database/file_database.db"
UPLOAD_FOLDER = 'generic_file_management/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def create_database(app):
    if not path.exists('generic_file_management/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


def create_app():
    app = Flask(__name__)
    secret_key = os.getenv('SECRET_KEY')
    if secret_key == 'None':
        secret_key = 'abc098def'

    app.config['SECRET_KEY'] = secret_key
    api = create_api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
    db.init_app(app)
    create_database(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/views')

    return app
