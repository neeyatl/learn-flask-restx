from .extensions import db
from .utils import get_fixture_json

def init_courses_db():
    from .models import Student, Course

    db.create_all()

    courses_json = get_fixture_json('courses.json')
    for course_json in courses_json:
        students = course_json.pop('students')

        course = Course(**course_json)
        db.session.add(course)

        db.session.add_all([
            Student(course=course, name=student['name'])
            for student in students
        ])

    db.session.commit()

def init_posts_db():
    from .models import Post, Comment

    db.create_all()

    posts_json = get_fixture_json('posts.json')
    for post_json in posts_json:
        comments = post_json.pop('comments')

        post = Post(**post_json)
        db.session.add(post)

        db.session.add_all([
            Comment(post=post, content=comment)
            for comment in comments
        ])
        db.session.commit()
