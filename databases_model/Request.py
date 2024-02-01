from databases_model.__libs__ import *


class Request(Base):
    __tablename__ = 'request'

    id = Column('id', Integer, primary_key=True, autoincrement=True)

    organisation = Column('organisation', ForeignKey('organisation.id'))
    calculation = Column('calculation', ForeignKey('calculation.id'))
    user = Column('user', ForeignKey('user.id'))
    status = Column('status', ForeignKey('request_status.id'))

    def __init__(self, organisation, calculation, user):
        self.organisation = organisation
        self.calculation = calculation
        self.user = user
        self.status = 1

    def __repr__(self):
        return f'<Request({self.id}: {self.organisation} {self.calculation} {self.user} {self.status})>'


class Organisation(Base):
    __tablename__ = 'organisation'

    id = Column('id', Integer, primary_key=True, autoincrement=True)

    organisation = Column('organisation', String)
    itn = Column('INT', String)

    def __init__(self, organisation, itn):
        self.organisation = organisation
        self.itn = itn

    def __repr__(self):
        return f'<Organisation({self.itn}: {self.organisation})>'


class Calculation(Base):
    __tablename__ = 'calculation'

    id = Column('id', Integer, primary_key=True, autoincrement=True)

    organisation = Column('organisation', String)
    itn = Column('itn', String)

    def __init__(self, organisation, itn):
        self.organisation = organisation
        self.itn = itn

    def __repr__(self):
        return f'<Organisation({self.itn}: {self.organisation})>'


class RequestStatus(Base):
    __tablename__ = 'request_status'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    status = Column('status', String)

    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return f'<Status({self.id}: {self.status})>'


