from os import path

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    # создание секретного ключа для шифрования куки и сессионных данных:
    app.config['SECRET_KEY'] = 'sfasgdsgdgds432fgnxfd55t'
    # SQLAlchemy БД локализирована по следующему пути:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  # инициализация БД

    from .auth import auth
    from .views import views

    # регистрация блюпринтов:
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')  # можно 'auth/', например

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    # при обращении пользователя на страницу, требующей регистрации
    # (@login_required), перенаправить на страницу логирования:
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# если БД нет по указаному пути, то создаем БД
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
