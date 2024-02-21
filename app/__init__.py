from flask import Flask
from .extensions import api, db
from .resources import ns

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # initialize extensions
    db.init_app(app)
    api.init_app(app)

    # register api resources
    api.add_namespace(ns)

    # register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
