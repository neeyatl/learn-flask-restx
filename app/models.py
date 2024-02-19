from .extensions import db


class Course(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students = db.relationship('Student', back_populates='course')


class Student(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    course_id = db.Column(db.ForeignKey('course.pk'), nullable=False)

    course = db.relationship('Course', back_populates='students')