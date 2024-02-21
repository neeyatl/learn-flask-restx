from flask import Flask

from config import Config

from .extensions import api, db
from .courses.resources import ns


def create_app():
    app = Flask(__name__)

    # configure app
    app.config.from_object(Config)

    # initialize extensions
    db.init_app(app)
    api.init_app(app)

    # register api resources
    api.add_namespace(ns)

    # register blueprints
    from app.main import bp as main_bp
    from app.blogs import bp as blog_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp)

    return app
