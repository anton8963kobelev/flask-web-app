# позволяет разделять проект на набор независимых модулей (при большой проекте)
from flask import Blueprint


views = Blueprint('views', __name__)  # __name__ - имя исполняемого модуля


@views.route('/')
def home():
    return '<h1>Home</h1>'
