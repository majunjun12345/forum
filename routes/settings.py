# no token

from flask import (
    request,
    render_template,
    Blueprint,
    redirect,
    url_for,
)

main = Blueprint('settings', __name__)

from routes import *
from models.user import User


@main.route('/', methods=['GET'])
def index():
    u = current_user()
    # token = new_csrf_token()
    return render_template('/settings/settings.html', user = u)


@main.route('/signature', methods=['POST'])
# @csrf_required
def signature():
    u = current_user()
    signature = request.form['signature']
    User.update(u.id, dict(
        personalized_signature=signature
    ))
    return redirect(url_for('.index'))


@main.route('/change_passwd', methods=['POST'])
def change_passwd():
    u = current_user()
    # password = request.form['old_pass']
    password = User.salted_password(request.form['old_pass'])
    if u.password == password:
        new_pass = User.salted_password(request.form['new_pass'])
        User.update(u.id, dict(
            password=new_pass
        ))
    else:
        print('密码不正确')
    return redirect(url_for('.index'))








