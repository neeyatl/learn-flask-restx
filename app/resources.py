from flask_restx import Resource, Namespace

from .extensions import db
from .models import Course, Student
from .api_models import (
    course_model, student_model, course_input_model, student_input_model
)

ns = Namespace('api', description='API')


@ns.route('/hello')
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}


@ns.route('/courses')
class CourseListAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()

    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    @ns.doc(responses={201: 'Course created'})
    def post(self):
        name = ns.payload['name']
        # validate name and sanitize it
        valid_name = name
        new_course = Course(name=valid_name)
        db.session.add(new_course)
        db.session.commit()
        return new_course, 201


@ns.route('/courses/<int:pk>')
@ns.doc(params={'pk': 'The course identifier'})
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    @ns.doc(responses={404: 'Course not found', 200: 'Course found'})
    def get(self, pk):
        course = Course.query.get_or_404(pk)
        return course


@ns.route('/students')
class StudentListAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()

    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    @ns.doc(responses={201: 'Student created'})
    def post(self):
        student_name = ns.payload['name']
        course_name = ns.payload['course_name']
        # validate name and sanitize it
        valid_student_name = student_name
        valid_course_name = course_name

        course = Course.query.filter_by(name=course_name).first()
        if not course:
            new_course = Course(name=valid_course_name)
            db.session.add(new_course)
            db.session.commit()
            course = Course.query.filter_by(name=valid_course_name).first()

        new_student = Student(name=valid_student_name, course=course)
        db.session.add(new_student)
        db.session.commit()
        return new_student, 201


@ns.route('/students/<int:pk>')
@ns.doc(params={'pk': 'The student identifier'})
class StudentAPI(Resource):
    @ns.marshal_with(student_model)
    @ns.doc(responses={404: 'Student not found', 200: 'Student found'})
    def get(self, pk):
        student = Student.query.get_or_404(pk)
        return student

    @ns.expect(course_input_model)
    @ns.marshal_with(student_model)
    @ns.doc(responses={200: 'Student updated', 404: 'Student not found'})
    def put(self, pk):
        student = Student.query.get_or_404(pk)
        name = ns.payload['name']
        # validate name and sanitize it
        valid_name = name
        student.name = valid_name
        db.session.commit()
        return student

    @ns.doc(responses={204: 'No Content', 404: 'Student not found'})
    def delete(self, pk):
        student = Student.query.get_or_404(pk)
        db.session.delete(student)
        db.session.commit()
        return {}, 204
