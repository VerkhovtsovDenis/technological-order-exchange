from flask import render_template, request, flash, redirect, session, abort, url_for
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from databases_model.Users import User
from flask import Blueprint
from scripts.menu import menu, admin_menu
from scripts.forms import LoginForm, SignupForm, UpdateUserFrom
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
    return User.get_by_id(user_id)


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
            flash(f'Верно указаны почта и пароль.', category='success')

            next = request.args.get('next')
            return redirect(next or url_for('urls.admin'))
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
            new_user = User(first_name, last_name, father_name, login, password)
            session.add(new_user)
            session.commit()

            flash('Пользователь зарегистрирован', category='success')
            return redirect(url_for('urls.login'))

    return render_template('signup.html', title="Регистрация", menu=menu, form=form)


@urls_blueprint.route('/admin')
@login_required
def admin():
    User._bootstrap()
    return render_template('admin//main.html', title='Панель администратора', adminmenu=admin_menu, user=current_user)


@urls_blueprint.route('/admin/users')
@login_required
def admin_users():
    users = User.get_all()
    return render_template('admin//users.html', title='Панель администратора: БД Пользователи', adminmenu=admin_menu, user=current_user, users=users)


@urls_blueprint.route('/admin/users/delete/<int:postID>')
@login_required
def admin_users_delete(postID):
    users = User.delete_by_id(postID)
    return url_for('urls.admin_users')


@urls_blueprint.route('/admin/users/update/<int:postID>', methods=['GET', 'POST'])
@login_required
def admin_users_update(postID):
    form = UpdateUserFrom()
    user = User.get_by_id(postID)
    form.fluid(user)

    return render_template('admin//edit.html', title='Панель администратора', adminmenu=admin_menu, user=current_user, form=form)


@urls_blueprint.route('/admin/organisation')
@login_required
def admin_organisation():
    return render_template('admin//organisation.html', title='Панель администратора: БД Организации', adminmenu=admin_menu, user=current_user)


@urls_blueprint.route('/admin/update:<table>:<id>')
@login_required
def update(table, id):

    return f'data was update, {table} {id}'
@urls_blueprint.route('/admin/delete:<table>:<id>')
@login_required
def delete(table, id):

    return f'data was delete, {table} {id}'

