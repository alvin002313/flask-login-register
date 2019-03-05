import os
from app import create_app
from app.models import User
from app.utils.decorators import login_required
from flask import render_template, request, session, redirect

config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)


@app.route("/", methods=["GET"])
def home():
    if session.get("uuid", False):
        return redirect("/protected")
    else:
        return render_template("home/index.html")


@app.route("/register", methods=["POST"])
def register():
    user = User(**dict(request.form))
    user.set_password(request.form.get("password"))
    context = {
        "message": "Ugurla qeydiyyatdan kecdiniz daxil olun"
    }
    return render_template("home/index.html", **context)


@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    user = User.find_by(email=email)
    if user.authenticate(password):
        session["uuid"] = user.id
        return redirect("/")
    else:
        context = {
            "message": "Email ve ya shifre yanlishdir",
            "error": True
        }
        return render_template("home/index.html", **context)


@app.route("/protected", methods=["GET"])
@login_required
def protected():
    return render_template("protected/index.html")


@app.route("/logout", methods=["GET"])
def logout():
    del session["uuid"]
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
