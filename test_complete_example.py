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
# 这里就是填充参数的
@pytest.mark.parametrize("a, b, result", [
    (3, 4, 12),
    (-2, 5, -10)
])
# 用这个参数 就会吧 a,b 都填充到里面去
def test_multiply(calc, a, b, result):
    assert calc.multiply(a, b) == result


# 异常测试
def test_divide_by_zero(calc):
    # raises 触发这个异常
    with pytest.raises(ValueError) as exc_info:
        # 10/0 肯定是错误的 ，所有会厨房触发这个异常
        calc.divide(10, 0)
    assert "The divisor cannot be zero" in str(exc_info.value)

# 也是标记 为 ui的分组
@pytest.mark.ui
def test_login_page():
    assert "login" in "login_page_content"
# 标记测试
@pytest.mark.slow
# 标记这个函数 会运行的很慢,所以下面我们就会模拟一个很慢的测试(这个mark 只是标记分组)
def test_slow_operation():
    import time
    # 使用 time库，模拟很慢的情况
    time.sleep(2)
    # assert 为 True,模拟测试通过

    assert True

@pytest.mark.fast
# 标记这个函数 会运行的很慢,所以下面我们就会模拟一个很慢的测试(这个mark 只是标记分组)
def test_fast_operation():
    # import time
    # # 使用 time库，模拟很慢的情况
    # time.sleep(2)
    # # assert 为 True,模拟测试通过
    assert True