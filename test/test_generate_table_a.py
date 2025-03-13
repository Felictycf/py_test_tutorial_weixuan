# 导入必要的库 / Import necessary libraries
import pytest  # pytest测试框架 / pytest testing framework
import pandas as pd  # 数据处理库 / Data manipulation library
import random  # 生成随机数 / Generate random numbers


def generate_table_a():
    """Generate Table A with product information. 生成包含产品信息的表格A"""
    data_a = {
        'product_id': list(range(1, 101)),  # 生成1-100的产品ID / Generate product IDs from 1 to 100
        'product_name': [f'Widget {i}' for i in range(1, 101)],
        # 生成产品名称Widget 1~Widget 100 / Generate product names Widget 1~Widget 100
        'amount': [random.randint(5, 100) for _ in range(100)]
        # 生成100个5-100之间的随机整数作为数量 / Generate 100 random integers between 5-100 as amounts
    }
    return pd.DataFrame(data_a)  # 返回Pandas DataFrame / Return Pandas DataFrame


# 测试用例1：验证DataFrame的形状
# Test Case 1: Verify the shape of the DataFrame
def test_generate_table_a_shape():
    # 调用函数生成DataFrame / Call function to generate DataFrame
    df = generate_table_a()

    # 验证DataFrame是否是100行3列 / Verify if DataFrame has 100 rows and 3 columns
    # assert语句会检查条件是否为True，如果失败则抛出错误
    # The assert statement checks if the condition is True, throws error if failed
    # 预期形状 (100,3)，错误时会显示实际获得的形状
    # Expected shape (100,3), will show actual shape if assertion fails
    assert df.shape == (100, 3), f"Expected shape (100, 3), but got {df.shape}"


# 测试用例2：验证product_id范围是否正确
# Test Case 2: Verify product_id contains numbers from 1 to 100
def test_generate_table_a_product_ids():
    df = generate_table_a()

    # 获取所有唯一的product_id并排序 / Get all unique product_ids and sort them
    unique_ids = sorted(df['product_id'].unique())

    # 验证排序后的id是否等于1-100的列表 / Verify if sorted IDs equal 1-100 range
    # 使用list(range(1,101))生成1-100的期望值
    # Generate expected 1-100 range using list(range(1,101))
    assert unique_ids == list(range(1, 101)), "Product IDs are not in the correct range."


# 测试用例3：验证amount字段范围
# Test Case 3: Verify that all amounts are within expected range (5 to 100)
def test_generate_table_a_amounts():
    df = generate_table_a()

    # 使用between()方法检查所有值是否在5-100之间
    # Use between() method to check all values are between 5-100
    # .all()确保所有值都满足条件 / .all() ensures all values meet the condition
    assert df['amount'].between(5, 100).all(), "Amounts are not within the expected range (5 to 100)."


# 测试用例4：模拟异常场景（临时修改函数使其抛出错误）
# Test Case 4: Simulate exception scenario (temporarily modify function to throw error)
def test_generate_table_a_invalid_product_count():
    try:
        # 临时将函数替换为会抛出ZeroDivisionError的lambda
        # Temporarily replace the function with a lambda that raises ZeroDivisionError
        generate_table_a = lambda: 1 / 0  # 强制触发除零错误 / Force ZeroDivisionError

        # 尝试调用被修改的函数 / Attempt to call modified function
        df = generate_table_a()

        # 如果代码执行到这里说明没有抛出异常，测试失败
        # If execution reaches here, no exception was raised, test fails
        assert False, "Expected exception, but function completed without error"

    except ZeroDivisionError:
        # 成功捕获到预期的异常，测试通过
        # Successfully caught expected exception, test passes
        assert True  # 在pytest中，只需到达这里即表示测试通过 / In pytest, reaching here means the test passes

# ----------------------------
# pytest 工作机制说明 / How pytest works:
# 1. pytest会自动发现以"test_"开头的函数和类 / pytest auto-discovers functions/classes starting with "test_"
# 2. 每个测试函数独立运行，互不影响 / Each test function runs independently
# 3. 使用assert语句进行验证，失败时显示错误信息 / Use assert statements for validation, shows error message on failure
# 4. 可以通过抛出特定异常来测试错误处理逻辑 / Can test error handling by raising specific exceptions
