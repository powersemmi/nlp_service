from os import environ, path
from dotenv import load_dotenv
load_dotenv()

basedir = path.abspath(path.dirname(__file__))


# Соединяемся с базой данных
class Config(object):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = (environ.get('DATABASE_URL') or
                               'sqlite:///' + path.join(basedir, 'app.sqlite') + '?check_same_thread=False') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning