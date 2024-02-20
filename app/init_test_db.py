from datetime import datetime
from .extensions import db
from .utils import get_fixture_json, get_random_item, randint

def init_courses_db():
    from .models import Student, Course

    db.create_all()

    courses_json = get_fixture_json('courses.json')
    for course_json in courses_json:
        students = course_json.pop('students')

        course = Course(**course_json)
        db.session.add(course)

        db.session.add_all([
            Student(
                course=course,
                enrollment_date=datetime.strptime(
                    student.pop('enrollment_date'),
                    "%Y-%m-%d"
                ).date(),
                **student
            )
            for student in students
        ])

    db.session.commit()

def init_posts_db():
    from .models import Post, Comment, Tag

    db.create_all()

    posts_json = get_fixture_json('posts.json')
    posts = []
    for post_json in posts_json:
        comments = post_json.pop('comments')

        post = Post(**post_json)
        db.session.add(post)
        posts.append(post)

        db.session.add_all([
            Comment(post=post, content=comment)
            for comment in comments
        ])
        db.session.commit()

    tags = [
        Tag(name='animals'),
        Tag(name='tech'),
        Tag(name='cooking'),
        Tag(name='writing'),
    ]

    for _ in range(randint(5, 10)):
        get_random_item(posts).tags.append(
            get_random_item(tags)
        )
    db.session.add_all(tags)
    db.session.commit()
