from .extensions import db


class Course(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship('Student', back_populates='course')

    def __repr__(self) -> str:
        return f'<Course "{self.name}">'


class Student(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course_id = db.Column(db.ForeignKey('course.pk'), nullable=False)

    course = db.relationship('Course', back_populates='students')

    def __repr__(self) -> str:
        return f'<Student "{self.name}">'


class Post(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __repr__(self) -> str:
        return f'<Post "{self.title}">'


class Comment(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.pk'))

    def __repr__(self) -> str:
        return f'<Comment "{self.content[:20]}...">'
