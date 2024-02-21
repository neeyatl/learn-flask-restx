from app.main import bp

@bp.route('/index')
def index():
    return '<h1>This is The Main Blueprint</h1>'
