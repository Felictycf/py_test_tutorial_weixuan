

# pytest Knowledge Documentation

---

## 1. Installation & Basic Usage

### Install pytest

```bash
pip install pytest
```

### First Test Case

Create `test_sample.py`:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

Run tests: （terminal run）

```bash
pytest test_sample.py -v
```

---

## 2. Test Structure & Assertions

### Test File Naming

- Files start/end with `test_` (e.g., `test_math.py` or `math_test.py`)
- Test functions start with `test_`

### Assertion Examples

```python
def test_strings():
    assert "hello" == "hello"
    assert "foo" in "foobar"

def test_lists():
    assert [1, 2] == [1, 2]
    assert 3 in [1, 2, 3]

def test_objects():
    class Person:
        def __init__(self, name):
            self.name = name
    p1 = Person("Alice")
    p2 = Person("Alice")
    assert p1.name == p2.name  # Passes
    # assert p1 == p2          # Fails
```

---

## 3. Fixture Mechanism

### Basic Fixture

```python
import pytest

@pytest.fixture
def database_connection():
    print("\nEstablishing DB connection")
    conn = "active_connection"
    yield conn
    print("\nClosing DB connection")

def test_query(database_connection):
    assert database_connection == "active_connection"
```

### Scope Control

```python
@pytest.fixture(scope="module")
def shared_resource():
    return "Shared resource"
```

---

## 4. Parametrized Tests

### Single Parameter

```python
import pytest

@pytest.mark.parametrize("input, expected", [
    (3, 9),
    (4, 16),
    (-2, 4)
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### Multiple Parameters

```python
@pytest.mark.parametrize("a, b, sum", [
    (1, 2, 3),
    (5, -1, 4),
    (0, 0, 0)
])
def test_add(a, b, sum):
    assert a + b == sum
```

---

## 5. Test Markers

### Custom Markers

```python
@pytest.mark.slow
def test_long_running():
    import time
    time.sleep(5)
    assert True

@pytest.mark.ui
def test_login_page():
    assert "login" in "login_page_content"
```

Run marked tests:

```bash
pytest -m slow
pytest -m "not slow"
```

---

## 6. Plugins & Extensions

### Popular Plugins

```bash
pip install pytest-cov    # Code coverage
pip install pytest-html   # HTML reports
pip install pytest-xdist  # Parallel testing
```

### Generate HTML Report

```bash
pytest --html=report.html
```

---

## 7. Test Coverage

### Configuration

1. Create `.coveragerc`:

```ini
[run]
source = my_project/
```

2. Run tests:

```bash
pytest --cov=my_project --cov-report=html
```

---

## 8. Exception Testing

### Testing Exceptions

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError) as exc_info:
        int("invalid")
    assert "invalid literal" in str(exc_info.value)
```

---

## 9. Common CLI Options

```bash
pytest -v               # Verbose mode
pytest -k "add"         # Run tests containing "add"
pytest --maxfail=2      # Stop after 2 failures
pytest --lf             # Run last failed tests
pytest --ff             # Run failures first then others
pytest -n 4             # Parallel testing with 4 workers
```

---

# Complete Test Example

Create `test_example.py`:

```python
import pytest

# Function under test
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Fixture
@pytest.fixture
def sample_data():
    return [2, 4, 6, 8]

# Parametrized test
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (20, 4, 5),
    (15, 3, 5)
])
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected

# Exception test
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero" in str(excinfo.value)

# Using fixture
def test_even_numbers(sample_data):
    for num in sample_data:
        assert num % 2 == 0

# Marked test
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(3)
    assert True
```

Run:

```bash
pytest test_example.py -v
pytest test_example.py -m slow
pytest test_example.py --html=report.html
```

---





# pytest 知识文档



---

## 1. 安装与基本使用

### 安装 pytest
```bash
pip install pytest
```

### 第一个测试用例
创建文件 `test_sample.py`:
```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```

运行测试：
```bash
pytest test_sample.py -v
```

---

## 2. 测试用例结构与断言

### 测试文件命名
- 文件名以 `test_` 开头或结尾（如 `test_math.py` 或 `math_test.py`）
- 测试函数以 `test_` 开头

### 断言示例 

就是我们之前讲的assert，进行判断  对不对等，之后在pycharm 里面运行就可以出现

```python
def test_strings():
    assert "hello" == "hello"
    assert "foo" in "foobar"

def test_lists():
    assert [1, 2] == [1, 2]
    assert 3 in [1, 2, 3]

def test_objects():
    class Person:
        def __init__(self, name):
            self.name = name
    p1 = Person("Alice")
    p2 = Person("Alice")
    assert p1.name == p2.name  # 通过
    # assert p1 == p2          # 失败
```

---

## 3. Fixture 机制

### 基本 Fixture
```python
import pytest

@pytest.fixture
def database_connection():
    print("\n建立数据库连接")
    conn = "active_connection"
    yield conn
    print("\n关闭数据库连接")

def test_query(database_connection):
    assert database_connection == "active_connection"
```

### 作用域控制
```python
@pytest.fixture(scope="module")
def shared_resource():
    return "共享资源"
```

---

## 4. 参数化测试

### 单个参数
```python
import pytest

@pytest.mark.parametrize("input, expected", [
    (3, 9),
    (4, 16),
    (-2, 4)
])
def test_square(input, expected):
    assert input ** 2 == expected
```

### 多个参数组合
```python
@pytest.mark.parametrize("a, b, sum", [
    (1, 2, 3),
    (5, -1, 4),
    (0, 0, 0)
])
def test_add(a, b, sum):
    assert a + b == sum
```

---

## 5. 标记测试 (Markers)

### 自定义标记
```python
@pytest.mark.slow
def test_long_running():
    import time
    time.sleep(5)
    assert True

@pytest.mark.ui
def test_login_page():
    assert "login" in "login_page_content"
```

运行指定标记的测试：
```bash
pytest -m slow
pytest -m "not slow"
```

---

## 6. 插件与扩展

### 常用插件
```bash
pip install pytest-cov    # 覆盖率
pip install pytest-html  # HTML报告
pip install pytest-xdist # 并行测试
```

### 生成 HTML 报告
```bash
pytest --html=report.html
```

---

## 7. 测试覆盖率

### 配置与使用
1. 创建 `.coveragerc` 文件：
```ini
[run]
source = my_project/
```

2. 运行测试：
```bash
pytest --cov=my_project --cov-report=html
```

---

## 8. 异常测试

### 测试异常抛出
```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error():
    with pytest.raises(ValueError) as exc_info:
        int("invalid")
    assert "invalid literal" in str(exc_info.value)
```

---

## 9. 常用命令行选项

```bash
pytest -v               # 详细模式
pytest -k "add"         # 运行包含 "add" 的测试
pytest --maxfail=2      # 失败2次后停止
pytest --lf             # 只运行上次失败的测试
pytest --ff             # 先运行失败测试，再运行其他
pytest -n 4            # 使用4个进程并行测试
```

---

# 完整测试示例

创建 `test_example.py`：
```python
import pytest

# 被测函数
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

# Fixture
@pytest.fixture
def sample_data():
    return [2, 4, 6, 8]

# 参数化测试
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (20, 4, 5),
    (15, 3, 5)
])
def test_divide_normal(a, b, expected):
    assert divide(a, b) == expected

# 异常测试
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "除数不能为零" in str(excinfo.value)

# 使用fixture
def test_even_numbers(sample_data):
    for num in sample_data:
        assert num % 2 == 0

# 标记测试
@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(3)
    assert True


```

运行：
```bash
pytest test_example.py -v
pytest test_example.py -m slow
pytest test_example.py --html=report.html
```

---

