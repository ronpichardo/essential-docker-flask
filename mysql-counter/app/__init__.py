from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__app__)
app.config.from_object('settings')
db = SQLAlchemy(app)

from counter import views