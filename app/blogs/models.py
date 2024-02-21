from app.extensions import db

post_tag = db.Table(
    'post_tag',
    db.Column('post_id', db.Integer, db.ForeignKey('post.pk')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.pk'))
)


class Post(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    tags = db.relationship('Tag', secondary=post_tag, backref='posts')

    def __repr__(self) -> str:
        return f'<Post "{self.title}">'


class Comment(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.pk'))

    def __repr__(self) -> str:
        return f'<Comment "{self.content[:20]}...">'


class Tag(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Tag "{self.name}">' 
