from flask import Flask
from blog.main_page.views import main_page
from blog.user.views import user
from blog.article.views import article
app=Flask(__name__)
def create_app() -> Flask:
    app=Flask(__name__)

    register_blueprints(app)
    app.run(
        host="0.0.0.0")

    return app
#
def register_blueprints(app:Flask):
    app.register_blueprint(main_page)
    app.register_blueprint(user)
    app.register_blueprint(article)


# @app.route('/')
# def hello():
#   return 'Hello World!'
# #
