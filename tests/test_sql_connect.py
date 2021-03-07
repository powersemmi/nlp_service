import pytest
import requests

from sqlalchemy import create_engine, engine
from os import environ, path
from dotenv import load_dotenv


load_dotenv()

def test_sql_connection() -> None:
    conn: engine.Engine = create_engine(environ.get('DATABASE_URL'))
    assert conn.connect()

def test_flask_conn() -> None:
    prod_host = environ.get('HOST')
    assert requests.get(prod_host+"/_test____conn").content.decode('utf-8') == "OK"