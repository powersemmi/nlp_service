import pytest
import sqlalchemy

def test_sql_connection() -> None:
    conn: sqlalchemy.engine.Engine = sqlalchemy.create_engine(conn_str, *args, **kwargs)
    assert conn.connect()
        