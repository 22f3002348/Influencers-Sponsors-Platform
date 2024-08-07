import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

dir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    dbdir = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    dbdir = os.path.join(dir, "../database")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(dbdir, "ispdb.sqlite3")
    DEBUG = True
