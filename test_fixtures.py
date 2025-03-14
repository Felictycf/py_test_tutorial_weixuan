import pytest
# 这个我们要注意 这个 fixture 就是一个提前设置信息的装饰器
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