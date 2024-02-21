from flask import Blueprint

bp = Blueprint('main', __name__)

from . import routes
from app.scripts import init_test_db
