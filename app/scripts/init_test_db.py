from datetime import datetime

from app.extensions import db
from app.main import bp
from app.utils import get_fixture_json, get_random_item, randint
from app.models import Post, Comment, Tag, Student, Course

def recreate_db():
    """
    Recreates the database by dropping all tables and then creating them again.
    """
    db.drop_all()
    db.create_all()

def init_courses_db():
    """
    Initializes the courses database by reading data from 'courses.json' fixture file.
    It iterates through the courses, creates Course objects, adds them to the database session,
    and then adds all the associated Student objects to the session before committing the changes.
    """
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
    """
    Initializes the posts database by reading data from 'posts.json' fixture file.
    It iterates through the posts, creates Post objects, adds them to the database session,
    and then adds all the associated Comment objects to the session before committing the changes.
    """
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

@bp.cli.command('recreate_test_db')
def recreate_test_db():
    """
    Command to recreate the test database.
    """
    recreate_db()
    init_courses_db()
    init_posts_db()
