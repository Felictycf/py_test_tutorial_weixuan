import pytest

@pytest.fixture
def database():
    print("\n--- Initializing a database connection ---")
    yield "db_connection"
    print("\n--- Close database connection ---")

def test_query(database):
    assert database == "db_connection"

@pytest.fixture(scope="module")
def shared_config():
    return {"timeout": 30}

def test_config(shared_config):
    assert shared_config["timeout"] == 30