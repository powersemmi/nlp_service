#!/usr/bin/env python3.8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app

if __name__ == '__main__':
    app.run()
