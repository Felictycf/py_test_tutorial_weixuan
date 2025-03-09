import pytest

def parse_int(s):
    if not s.isdigit():
        raise ValueError("无效的数字字符串")
    return int(s)

def test_valid_input():
    assert parse_int("42") == 42

def test_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        parse_int("foo")
    assert "无效的数字字符串" in str(exc_info.value)