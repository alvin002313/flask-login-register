from app.models import User
from flask import session, redirect, request


def login_required(func):
    def wrapper():
        user_id = session.get("uuid")
        if user_id:
            user = User.find(user_id)
            if user:
                request.user = user
                return func()
        else:
            return redirect("/")

    return wrapper

