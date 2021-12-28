# Blueprint - позволяет разделять проект на набор независимых модулей
# flash - отправка моментальных сообщений
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .models import User

auth = Blueprint('auth', __name__)  # __name__ - имя исполняемого модуля


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Логирование прошло успешно', category='success')
                # запомнить текущего пользователя в сессии:
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Неверный пароль, попробуйте еще раз', category='error')
        else:
            flash('Email не существует', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email уже существует', category='error')
        elif len(email) < 4:
            flash('Email должен быть длиннее 3 символов', category='error')
        elif len(first_name) < 2:
            flash('Имя должен быть длиннее 1 символов', category='error')
        elif len(password1) < 8:
            flash('Пароль должен быть длиннее 7 символов', category='error')
        elif password1 != password2:
            flash('Пароли не совпадают', category='error')
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method='sha256'),
            )
            db.session.add(new_user)
            db.session.commit()
            flash('Пользователь успешно создан', category='success')
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template('sign_up.html', user=current_user)
