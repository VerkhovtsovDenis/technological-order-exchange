from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bf612bd68decb030446c2b93e9dc8095f95d8bd35d0f87c2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:1234@localhost:5432/postgres'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)


db = SQLAlchemy(app)
Base = db.Model
session = db.session
