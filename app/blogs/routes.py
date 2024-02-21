from flask import render_template
from app.blogs import bp
from app.blogs.models import Comment, Post, Tag

@bp.route('/blogs')
def index():
    posts = Post.query.all()
    return render_template('blogs/index.html', posts=posts)

@bp.route('/blogs/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blogs/show_post.html', post=post)
