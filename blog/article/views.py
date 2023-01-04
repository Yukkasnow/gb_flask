from flask import Blueprint

article=Blueprint('article', __name__ , static_folder='../static', url_prefix='/article')

@article.route('/')
def index():
    return "Hello article!"