import uuid
from functools import wraps

from flask import (
    session,
    request,
    abort,
    redirect,
    url_for,
)
# import redis

from models.user import User
from utils import log


# def current_user():
#     uid = session['user_id']
#     u = User.one(id=uid)
#     return u


def current_user():
    uid = session.get('user_id', '')
    if uid:
        u = User.one(id=uid)
        return u
    else:
        # u = User()
        # print('u majun:', u.username)
        return None


def login_required(route_function):
    @wraps(route_function)
    def f():
        u = current_user()
        if u is None:
            log('非登录用户')
            return redirect(url_for('topic.index'))
        else:
            return route_function()

    return f


csrf_tokens = dict()
# redis 自动转码
# r = redis.StrictRedis(charset="utf-8", decode_responses=True)


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        u = current_user()
        # if token in csrf_tokens and csrf_tokens[token] == u.id:
        # log('check token', token, u.id, r.exists(token), r.get(token))
        # if r.exists(token) and r.get(token) == u.id:
        # r.delete(token)
        if token in csrf_tokens:
            # 这个操作能够删除键，并返回键对应的值
            # 访问每个权限页面，它的 token 都不一样，所以，边创建边删除
            uid = csrf_tokens.pop(token)
            if uid == u.id:
                return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_tokens[token] = u.id
    # r.set(token, u.id)
    # log('new token', token, u.id)
    return token
