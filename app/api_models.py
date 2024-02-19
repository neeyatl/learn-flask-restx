from flask_restx import fields

from .extensions import api

course_model = api.model('Course', {
    'pk': fields.Integer,
    'name': fields.String,
    'students': fields.List(fields.Nested(
        api.model('Student', {
            'pk': fields.Integer,
            'name': fields.String,
        })
    )),
})

course_input_model = api.model('CourseInput', {
    'name': fields.String,
})

student_model = api.model('Student', {
    'pk': fields.Integer,
    'name': fields.String,
    'course': fields.Nested(course_model),
})

student_input_model = api.model('StudentInput', {
    'name': fields.String,
    'course_name': fields.String,
})
