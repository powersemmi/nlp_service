from typing import Optional
import requests

from sqlalchemy import create_engine, engine
from os import environ, path
from dotenv import load_dotenv


load_dotenv()

def test_sql_connection() -> None:
    conn_str: Optional[str] = environ.get('DATABASE_URL')
    assert isinstance(conn_str, str), TypeError(".env pram 'DATABASE_URL' is not defiend")
    conn: engine.Engine = create_engine(conn_str)
    assert conn.connect()

def test_flask_conn() -> None:
    """Runtime test"""
    prod_host: Optional[str] = environ.get('HOST')
    assert isinstance(prod_host, str), TypeError(".env pram 'HOST' is not defiend")
    assert requests.get(prod_host+"/_test____conn").content.decode('utf-8') == "OK", RuntimeError("Server is not started")