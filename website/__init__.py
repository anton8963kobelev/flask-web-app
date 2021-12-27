from flask import Flask


def create_app():
    app = Flask(__name__)
    # создание секретного ключа для шифрования куки и сессионных данных:
    app.config['SECRET_KEY'] = 'sfasgdsgdgds432fgnxfd55t'

    from .views import views
    from .auth import auth

    # регистрация блюпринтов:
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  # можно 'auth/', например

    return app
