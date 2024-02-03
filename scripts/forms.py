from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    login = StringField('Логин: ', validators=[Length(min=4, max=30, message='Логин должен быть от 10 до 30 символов')])
    pwd = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100)])
    remember = BooleanField('Запомнить', default=False)
    submit = SubmitField('Войти')


class SignupForm(FlaskForm):
    last_name = StringField('Фамилия: ', validators=[Length(min=4, max=30, message='Фамилия должна быть от 4 до 30 символов')])
    first_name = StringField('Имя: ', validators=[Length(min=4, max=30, message='Имя должно быть от 4 до 30 символов')])
    father_name = StringField('Отчество: ', validators=[Length(min=4, max=30, message='Отчество должно быть от 4 до 30 символов')])
    login = StringField('Логин: ', validators=[Length(min=4, max=30, message='Логин должен быть от 10 до 30 символов')])
    pwd = PasswordField('Пароль: ', validators=[DataRequired(), Length(min=4, max=100)])
    pwd2 = PasswordField('Повтор пароля: ', validators=[DataRequired(), EqualTo('pwd', message='Пароли не совпадают'),
                                                        Length(min=4, max=100)])
    submit = SubmitField('Регистрация')