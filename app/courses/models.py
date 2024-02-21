from app.extensions import db


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

    email = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer)
    enrollment_date = db.Column(db.Date)
    active = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f'<Student "{self.name}">'
