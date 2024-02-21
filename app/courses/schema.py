from flask_restx import fields

from app.extensions import api

course_model = api.model('Course', {
    'pk': fields.Integer,
    'name': fields.String,
})

student_model = api.model('Student', {
    'pk': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'age': fields.Integer,
    'enrollment_date': fields.Date,
    'active': fields.Boolean,
})

courses_model = course_model.clone('Course', {
    'students': fields.List(fields.Nested(student_model)),
})

course_input_model = api.model('CourseInput', {
    'name': fields.String,
})

students_model = student_model.clone('Student', {
    'course': fields.Nested(course_model),
})

student_input_model = api.model('StudentInput', {
    'name': fields.String,
    'course_name': fields.String,
})
