#!/usr/bin/env python3.8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import nlp_service
from config import Config



if __name__ == '__main__':
    nlp_service.app = nlp_service.create_app(Config)
    nlp_service.db = nlp_service.create_db(nlp_service.app)
    migrate = Migrate(nlp_service.app, nlp_service.db)

    from nlp_service.routing import *

    nlp_service.app.run()
