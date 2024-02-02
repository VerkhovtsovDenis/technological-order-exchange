import site
from flask import render_template, request, flash, redirect, session, abort, url_for
from flask_login import login_user, current_user
from databases_model.Users import User
from site import *
from flask import Blueprint


urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def index():
    return render_template('index.html', menu=menu)


@urls_blueprint.route('/about')
def about():
    return render_template('about.html', title="О сайте", menu=menu)



@urls_blueprint.route('/login', methods=['GET', 'POST'])
def login():


    if current_user.is_authenticated:
        return redirect(url_for('profile', username=current_user.get_user()))
    form = LoginForm()

    if form.validate_on_submit():

        user = User.get_by_login(form.login.data)

        if user and user.pwd == form.pwd.data:
            login_user(user.login)

            return redirect(request.args.get('next') or url_for('admin', username=user.email.split('@')[0]))


        flash(f'Неверно указана почта или пароль.', category='error')

    return render_template('login.html', title='Авторизация', menu=menu, form=form)




@urls_blueprint.route('/login')
def about():
    return render_template('login.html', title="Авторизация", menu=menu)




@urls_blueprint.route('/registration')
def about():
    return render_template('registration.html', title="Регистрация", menu=menu)
