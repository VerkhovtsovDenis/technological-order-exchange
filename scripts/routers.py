from flask import render_template, request, flash, redirect, session, abort, url_for
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from databases_model.Users import User
from flask import Blueprint
from scripts.menu import menu
from scripts.forms import LoginForm, SignupForm
from flask_login import login_user, login_required, current_user, logout_user
from create_app import session


from flask_login import LoginManager
from create_app import app
from databases_model import User

login_manager = LoginManager()
login_manager.login_view = 'urls.login'
login_manager.login_message = 'Пожалуйста, пройдите авторизацию для доступа к странице.'
login_manager.login_message_category = 'info'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    print('user_id = ', user_id)
    return User.get_by_login(user_id)


urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def index():
    return render_template('index.html', menu=menu)


@urls_blueprint.route('/about')
def about():
    return render_template('about.html', title="О сайте", menu=menu)

@urls_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(1)

    if form.validate_on_submit():
        print(2)

        login = form.login.data
        password = form.pwd.data
        remember = form.remember.data

        user = User.get_by_login(login=login)
        print(3, user)

        if user and check_password_hash(user.password, password):
            login_user(user, remember=remember)
            print(4)
            flash(f'Верно указаны почта или пароль.', category='success')

            return redirect(url_for('urls.admin'))
        flash(f'Неверно указана почта или пароль.', category='error')

    return render_template('login.html', title='Авторизация', menu=menu, form=form)


@urls_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из аккаунта', category='success')
    return redirect(url_for('urls.login'))


@urls_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        login = form.login.data
        password = form.pwd.data

        user = User.get_by_login(login)

        if user and user.password == password:
            flash('Пользователь уже зарегистрирован', category='into')
            return redirect(url_for('urls.login'))
        else:
            first_name = form.first_name.data
            last_name = form.last_name.data
            father_name = form.father_name.data

            # TODO gender chose
            new_user = User(first_name, last_name, father_name, login,
                            password=generate_password_hash(password, method='pbkdf2'))
            session.add(new_user)
            session.commit()

            flash('Пользователь зарегистрирован', category='success')
            return redirect(url_for('urls.login'))

    return render_template('signup.html', title="Регистрация", menu=menu, form=form)


@urls_blueprint.route('/admin/<login>')
@login_required
def admin(login):
    print(login)
    return render_template('admin.html', title='Админ', menu=menu, user=current_user)

