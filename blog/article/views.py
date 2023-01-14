from flask import Blueprint, render_template
from blog.data.base import ARTICLES

article=Blueprint('article', __name__ , static_folder='../static', url_prefix='/article')

@article.route('/')
def article_list():
    return render_template('article/list.html', articles=ARTICLES)
    # artic_lst=[]
    # for article_id in ARTICLES:
    #     artic_lst.append(ARTICLES[article_id]["title"])
    #
    # return render_template('article/list.html', artic_lst=artic_lst)

@article.route('/<int:pk>')
def article_detail(pk:int):
    article_id=pk
    article_title=ARTICLES[article_id]["title"]
    art_author=ARTICLES[article_id]["author"]
    text=ARTICLES[article_id]["text"]
    return render_template('article/detail.html', article_title=article_title, art_author=art_author, text=text)