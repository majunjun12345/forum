from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    make_response,
    send_from_directory,
)
# from werkzeug.utils import secure_filename
from models.user import User
import os
import uuid
# from flask_login import logout_user

from routes import *
# from utils import log

main = Blueprint('index', __name__)


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""


# @main.route("/")
# def index():
#     return render_template("register.html")


@main.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = request.form
        # 用类函数来判断
        u = User.register(form)
        return redirect(url_for('index.login'))


@main.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = request.form
        u = User.validate_login(form)
        # print('login u', u)
        if u is None:
            # 转到 topic.index 页面
            return redirect(url_for('.register'))
        else:
            # session 中写入 user_id
            session['user_id'] = u.id
            # print('login', session)
            # 设置 cookie 有效期为 永久
            session.permanent = True
            return redirect(url_for('topic.index'))


@main.route('/logout', methods=['GET'])
def logout():
    u = current_user()
    session.pop('user_id', None)
    return redirect(url_for('index.login'))


@main.route('/profile')
@login_required
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('.index'))
    else:
        topicss = User.topics(u.id)
        reply_topics = User.replied_topics(u.id)
        return render_template('profile.html', user=u, topics=topicss, reply_topics=reply_topics)


@main.route('/user/<string:id>')
def user(id):
    u = User.one(id=id)
    topicss = User.topics(u.id)
    # print('u.id:', u.id)
    reply_topics = User.replied_topics(u.id)
    if u is None:
        return redirect(url_for('.index'))
    else:
        return render_template('profile.html', user=u, topics=topicss, reply_topics=reply_topics)


def valid_suffix(suffix):
    valid_type = ['jpg', 'JPG', 'png', 'PNG', 'jpeg', 'JPEG', 'BMP', 'gif', 'GIF']
    return suffix in valid_type


@main.route('/image/add', methods=["POST"])
def add_img():
    # print('majun add_img()')
    # file 是一个上传的文件对象
    file = request.files['avatar']
    suffix = file.filename.split('.')[-1]
    # print('suffix:', suffix)
    if valid_suffix(suffix):
        # 上传的文件一定要用 secure_filename 函数过滤一下名字
        # ../../../../../../../root/.ssh/authorized_keys
        # filename = secure_filename(file.filename)
        filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
        file.save(os.path.join('user_image', filename))
        u = current_user()
        User.update(u.id, dict(
            user_image='/uploads/{}'.format(filename)
        ))

    return redirect(url_for(".profile"))


# send_from_directory
# nginx 静态文件
@main.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory('user_image', filename)
