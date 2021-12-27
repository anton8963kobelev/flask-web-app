# позволяет разделять проект на набор независимых модулей (при большой проекте)
from flask import Blueprint


auth = Blueprint('auth', __name__)  # __name__ - имя исполняемого модуля


@auth.route('/login')
def login():
    return '<h1>LogIn</h1>'


@auth.route('/logout')
def logout():
    return '<h1>LogOut</h1>'


@auth.route('/sign-up')
def sign_up():
    return '<h1>SignUp</h1>'
