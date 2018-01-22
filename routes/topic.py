from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)
from utils import log
from routes import *
# import json

from models.topic import Topic
from models.board import Board

main = Blueprint('topic', __name__)


@main.route("/")
# @login_required
def index():
    u = current_user()
    # log('用户名：', u.username)
    board_id = request.args.get('board_id', 'all')
    if board_id == 'all':
        ms = Topic.all()
        ms = sorted(ms, key=lambda topic: topic.created_time, reverse=True)
    else:
        ms = Topic.all(board_id=board_id)
        ms = sorted(ms, key=lambda topic: topic.created_time, reverse=True)

    # token = new_csrf_token()
    bs = Board.all()
    # return render_template("topic/index.html", ms=ms, token=token, bs=bs, bid=board_id, user=u)
    return render_template("topic/index.html", ms=ms, bs=bs, bid=board_id, user=u)


@main.route('/<string:id>')
# @login_required
def detail(id):
    m = Topic.find(id=id)
    u = current_user()
    board_name = m.board()
    # pub_time = m.pub_time()
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m, user=u, board = board_name)


@main.route("/add", methods=["POST"])
@login_required
# @csrf_required
def add():
    form = request.form
    u = current_user()
    Topic.new(form, user_id=u.id)
    return redirect(url_for('.index'))


@main.route("/delete")
@login_required
# @csrf_required
def delete():
    id = request.args.get('id')
    u = current_user()
    print('删除 topic 用户是', u, id)
    Topic.delete(id)
    return redirect(url_for('.index'))


@main.route("/new")
@login_required
def new():
    board_id = request.args.get('board_id')
    # token = new_csrf_token()
    bs = Board.all()
    # return render_template("topic/new.html", bs=bs, token=token, bid=board_id)
    return render_template("topic/new.html", bs=bs, bid=board_id)
