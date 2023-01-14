from flask import Blueprint, render_template
from flask_login import login_required
from werkzeug.exceptions import NotFound
from blog.models import Article, User

article=Blueprint('article', __name__ , static_folder='../static', url_prefix='/article')

    
@article.route('/')
def article_list():
    articles = Article.query.all()
    return render_template(
        'article/list.html',
        articles=articles,
    )    

@article.route('/<int:pk>')
@login_required
def article_detail(pk:int):
    selected_article = Article.query.filter_by(id=pk).one_or_none()
    selected_author = User.query.filter_by(id=selected_article.author_id).one_or_none()
    if not selected_article:
        raise NotFound(f"Article #{pk} doesn't exist!")

    return render_template(
        'article/detail.html',
        article=selected_article,
        author=selected_author
    )

    