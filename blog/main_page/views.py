from flask import Blueprint,render_template

main_page=Blueprint('main_page', __name__ , static_folder='../static')

@main_page.route('/')
def index():
    hello="Hello World!"
    return render_template('main_page/main_page.html',hello=hello)