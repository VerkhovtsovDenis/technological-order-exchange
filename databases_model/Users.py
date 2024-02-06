from datetime import datetime
from random import randint

from mimesis.builtins import RussiaSpecProvider
from sqlalchemy import func
from werkzeug.security import generate_password_hash

from create_app import session
from databases_model.__libs__ import *



class User(Base):
    __tablename__ = 'user'

    id = Column('id', Integer, primary_key=True, autoincrement=True)

    first_name = Column('first_name', String)
    last_name = Column('last_name', String)
    father_name = Column('father_name', String)

    login = Column('login', String)
    password = Column('password', String)

    last_update = Column('last_update', DateTime, server_default=func.now())

    role = Column('role', ForeignKey('user_role.id'))
    status = Column('status', ForeignKey('user_status.id'))

    gender = Column('gender', CHAR)

    def __init__(self, first_name, last_name, father_name, login, password, role=1, status=1, gender='М'):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.login = login
        self.password = generate_password_hash(password, method='pbkdf2')

        timestamp = datetime.now()
        self.last_update = timestamp.strftime('%Y-%m-%d %H:%M:%S')

        self.role = role
        self.status = status
        self.gender = gender

    def __repr__(self):
        return f'<User({self.login}: {self.last_name} {self.first_name} {self.father_name} {self.role})>'

    @staticmethod
    def _bootstrap(count=50, locale='ru'):
        from mimesis.providers import Person
        from mimesis.enums import Gender

        person = Person(locale)
        p = RussiaSpecProvider()
        patients = []
        for _ in range(count):

            a = randint(0, 2)
            sex = Gender.MALE if randint(0, 2) == 0 else Gender.FEMALE

            patient = User(
                first_name = person.name(gender=sex),
                last_name = person.surname(gender=sex),
                father_name = p.patronymic(gender=sex),
                login = person.email().split('@')[0],
                password = '1234',
                role=1,
                status=1,
                gender ='М' if sex == Gender.MALE else 'Ж')
            patients.append(patient)
            print(f'{_}-й был сгенерирован')

        for patient in patients:
            session.add(patient)
        session.commit()


    def get(self):
        return self

    def get_id(self):
        return str(self.id)

    @staticmethod
    def get_by_login(login):
        return User.query.filter_by(login=login).first()

    @staticmethod
    def get_by_id(user_id: int):
        return User.query.get(user_id)

    @staticmethod
    def get_all():
        Query = User.query
        Query = Query.join(UserRole).add_column(UserRole.role)
        Query = Query.join(UserStatus).add_column(UserStatus.status)
        return Query

    @staticmethod
    def delete_by_id(postID):
        User.query.filter_by(id=postID).delete()
        session.commit()
        return User.get_all()


    @staticmethod
    def is_authenticated(self):
        return True

    def is_active(self):
        return self.status == 1

    @staticmethod
    def is_anonymous(self):
        return False


class UserRole(Base):
    __tablename__ = 'user_role'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    role = Column('role', String)

    def __init__(self, role):
        self.role = role

    def __repr__(self):
        return f'<Role({self.id}: {self.role})>'


class UserStatus(Base):
    __tablename__ = 'user_status'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String)

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return f'<Status({self.id}: {self.status})>'
