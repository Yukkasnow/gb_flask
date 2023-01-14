from flask import Blueprint, render_template
from blog.data.base import USERS

user=Blueprint('user', __name__ , static_folder='../static', url_prefix='/user')


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)

@user.route('/<int:pk>')
def user_detail(pk:int):
    user_name=USERS[pk]
    return render_template('user/detail.html', user_name=user_name)