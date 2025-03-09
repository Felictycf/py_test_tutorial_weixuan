# 被测函数
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_string_comparison():
    assert "hello".upper() == "HELLO"

def test_list_operations():
    assert [1, 2, 3] + [4] == [1, 2, 3, 4]