from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *
from models.mail import Mail

main = Blueprint('mail', __name__)


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    print('form:', form)
    Mail.new(form, sender_name=u.username)
    return redirect(url_for(".index"))


@main.route("/", methods=["GET"])
def index():
    u = current_user()
    send_mail = Mail.all(sender_name=u.username)
    received_mail = Mail.all(receiver_name=u.username)
    t = render_template(
        "mail/index.html",
        sends=send_mail,
        receives=received_mail,
        user=u,
    )
    return t


@main.route("/view/<string:id>")
def view(id):
    mail = Mail.one(id=id)
    if current_user().username in [mail.receiver_name, mail.sender_name]:
    # if current_user().id == mail.receiver_id and current_user().id == mail.sender_id:
        return render_template("mail/detail.html", mail=mail)
    else:
        return redirect(url_for(".index"))
