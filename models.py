from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    url = db.Column('URL', db.String())
