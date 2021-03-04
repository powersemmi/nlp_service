import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


# Соединяемся с базой данных
class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{host}/{db}'.format(user=os.environ.get('PG_USER'),
                                                                                    pw=os.environ.get('PG_PASSWD'),
                                                                                    host=os.environ.get('PG_HOST'),
    
                                                                                    db=os.environ.get('PG_DB'))
    # SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
    #                            'sqlite:///' + os.path.join(basedir, 'app.sqlite')) + '?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # silence the deprecation warning