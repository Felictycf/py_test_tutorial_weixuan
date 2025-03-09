import pytest

@pytest.fixture
def database():
    print("\n--- 初始化数据库连接 ---")
    yield "db_connection"
    print("\n--- 关闭数据库连接 ---")

def test_query(database):
    assert database == "db_connection"

@pytest.fixture(scope="module")
def shared_config():
    return {"timeout": 30}

def test_config(shared_config):
    assert shared_config["timeout"] == 30