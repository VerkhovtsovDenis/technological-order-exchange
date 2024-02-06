from databases_model import *
from create_app import session


def set_data():
    request_status = []
    request_status += [RequestStatus('Created')]
    request_status += [RequestStatus('In verification')]
    request_status += [RequestStatus('On approval')]
    request_status += [RequestStatus('On pause')]
    request_status += [RequestStatus('Closed')]

    organisations = []
    organisations += [Organisation('ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ АВТОНОМНОЕ ОБРАЗОВАТЕЛЬНОЕ УЧРЕЖДЕНИЕ '
                                  'ВЫСШЕГО ОБРАЗОВАНИЯ "ДАЛЬНЕВОСТОЧНЫЙ ФЕДЕРАЛЬНЫЙ УНИВЕРСИТЕТ',
                                  '2536014538')]
    organisations += [Organisation('ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ "СТАРТАП-СТУДИЯ ДВФУ"',
                                  '2540273052')]
    organisations += [Organisation('ФОНД ПОДДЕРЖКИ ТЕХНОЛОГИЧЕСКОГО ПРЕДПРИНИМАТЕЛЬСТВА ДАЛЬНЕВОСТОЧНОГО '
                                  'ФЕДЕРАЛЬНОГО УНИВЕРСИТЕТА',
                                  '2540230267')]

    role = []
    role += [UserRole('Модератор')]
    role += [UserRole('Заявитель')]
    role += [UserRole('Сотрудник')]
    role += [UserRole('Студент')]

    user_status = []
    user_status += [UserStatus('Активная')]
    user_status += [UserStatus('В архиве')]

    user = []
    user += [User('Верховцов', 'Денис', 'Олегович', 'verkhovtcov.do', '1234',
                  1, 1, 'М')]

    for item in request_status + organisations + role + user_status:
        session.add(item)
    session.commit()

    for item in user:
        session.add(item)
    session.commit()



if __name__ == '__main__':
    set_data()
    print('data set successful')
