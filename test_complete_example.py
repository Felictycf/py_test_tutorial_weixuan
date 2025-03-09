import pytest


# Class under test
class Calculator:
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("The divisor cannot be zero")
        return a / b


# Fixture
@pytest.fixture
def calc():
    return Calculator()


# 参数化测试
@pytest.mark.parametrize("a, b, result", [
    (3, 4, 12),
    (-2, 5, -10)
])
def test_multiply(calc, a, b, result):
    assert calc.multiply(a, b) == result


# 异常测试
def test_divide_by_zero(calc):
    with pytest.raises(ValueError) as exc_info:
        calc.divide(10, 0)
    assert "The divisor cannot be zero" in str(exc_info.value)


# 标记测试
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(2)
    assert True