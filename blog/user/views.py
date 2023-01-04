from flask import Blueprint

user=Blueprint('user', __name__ , static_folder='../static', url_prefix='/user')

@user.route('/')
def index():
    return "Hello user!"