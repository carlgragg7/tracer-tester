import pytest

from tests import server

@pytest.fixture(scope="session", autouse=True)
def db_connection():
    conn = server.connect()
    yield conn
    server.disconnect(conn)
