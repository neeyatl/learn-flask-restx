from flask import render_template
from app.blogs import bp
from app.blogs.models import Comment, Post, Tag

@bp.route('/blogs')
def index():
    posts = Post.query.all()
    return render_template('blogs/index.html', posts=posts)
