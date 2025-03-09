import pytest

@pytest.mark.parametrize("input, expected", [
    (1, 2),
    (3, 6),
    (5, 10)
])
def test_double(input, expected):
    assert input * 2 == expected

@pytest.mark.parametrize("a, b, max_value", [
    (10, 20, 20),
    (30, 15, 30),
    (-5, 5, 5)
])
def test_max(a, b, max_value):
    assert max(a, b) == max_value