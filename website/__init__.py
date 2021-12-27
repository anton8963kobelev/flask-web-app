from flask import Flask


def create_app():
    app = Flask(__name__)
    # создание секретного ключа для шифрования куки и сессионных данных:
    app.config['SECRET_KEY'] = 'sfasgdsgdgds432fgnxfd55t'
    return app
