from flask import Blueprint

main_page=Blueprint('main_page', __name__ , static_folder='../static')

@main_page.route('/')
def index():
    return "Hello world!"