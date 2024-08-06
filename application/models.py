import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dir = os.path.abspath(os.path.dirname(__file__))
DB_DIR= os.path.join(dir, "../database")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(DB_DIR, "testdb.sqlite3") 
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()
