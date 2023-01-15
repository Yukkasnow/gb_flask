import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


@click.command('init-db')
def init_db():
    from wsgi import app

    # import models for creating tables
    from blog.models import User,Article

    db.create_all(app=app)


@click.command('create-init-article')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name2@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()
    from blog.models import Article

    from wsgi import app

    with app.app_context():
        db.session.add(
            Article(title="Горные лыжи", text="Горные лыжи: Проснуться утром, собрать вещи и ехать на горнолыжный курорт, "\
                 "кататься на лыжах, наслаждаться видами, пить горячий глинтвейн, есть оленину, ходить по магазинам,"\
                 " покупать теплые вещи, спать в теплой кровати, читать книги, смотреть фильмы, ходить на вечеринки.",
       author_id=1)
        )
        
        db.session.commit()
    with app.app_context():
        db.session.add(
            User(email="admin@admin.com",
                 password=generate_password_hash('admin'))
        )

        db.session.commit()
