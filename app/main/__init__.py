from flask import Blueprint

bp = Blueprint('main', __name__)

from . import routes as _
from app.scripts import init_test_db as _
