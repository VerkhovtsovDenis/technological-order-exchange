from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.fields.choices import RadioField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired

from databases_model import User


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
    # gender = StringField('Пол <М/Ж>: ', validators=[Length(min=1, max=1)])
    gender = SelectField('Gender', coerce=int, choices=[  # cast val as int
        (0, 'Male'),
        (1, 'Female'),
    ])
    submit = SubmitField('Регистрация')

class UpdateUserFrom(FlaskForm):
    last_name = StringField('Фамилия: ',
                            validators=[Length(min=4, max=30, message='Фамилия должна быть от 4 до 30 символов')])
    first_name = StringField('Имя: ',
                             validators=[Length(min=4, max=30, message='Имя должно быть от 4 до 30 символов')])
    father_name = StringField('Отчество: ', validators=[
        Length(min=4, max=30, message='Отчество должно быть от 4 до 30 символов')])

    gender = SelectField('Gender', coerce=int, choices=[  # cast val as int
        (0, 'Male'),
        (1, 'Female'),
    ])

    login = StringField('Логин: ',
                        validators=[Length(min=4, max=30, message='Логин должен быть от 10 до 30 символов')])
    # TODO - как сделать выборку из бд?
    # role = ...
    role = SelectField('role', coerce=int, choices=[...])
    status = ...
    submit = SubmitField('Обновить')

    def fluid(self, user: User):
        if isinstance(user, User):
            self.last_name.data = user.last_name
            self.first_name.data = user.first_name
            self.father_name.data = user.father_name
            self.login.data = user.login
            self.gender.data = user.gender
            self.role.data = user.role
        else:
            raise Exception("TypeError")


