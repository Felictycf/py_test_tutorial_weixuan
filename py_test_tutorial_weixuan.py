import pytest

def parse_int(s):
    if not s.isdigit():
        raise ValueError("Invalid numeric string")
    return int(s)

def test_valid_input():
    assert parse_int("42") == 42

def test_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        parse_int("foo")
    assert "Invalid numeric string" in str(exc_info.value)