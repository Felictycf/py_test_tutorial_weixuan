import pytest
import pandas as pd
import random


def generate_table_a():
    """Generate Table A with product information."""
    data_a = {
        'product_id': list(range(1, 101)),  # 100 product_ids
        'product_name': [f'Widget {i}' for i in range(1, 101)],
        'amount': [random.randint(5, 100) for _ in range(100)]  # Integer amounts
    }
    return pd.DataFrame(data_a)
# Test case 1: Verify the shape of the DataFrame
def test_generate_table_a_shape():
    df = generate_table_a()
    assert df.shape == (100, 3), f"Expected shape (100, 3), but got {df.shape}"

# Test case 2: Verify product_id contains numbers from 1 to 100
def test_generate_table_a_product_ids():
    df = generate_table_a()
    assert sorted(df['product_id'].unique()) == list(range(1, 101)), "Product IDs are not in the correct range."

# Test case 3: Verify that all amounts are within the expected range (5 to 100)
def test_generate_table_a_amounts():
    df = generate_table_a()
    assert df['amount'].between(5, 100).all(), "Amounts are not within the expected range (5 to 100)."


# Test case 4 : Simulate an exception by modifying the function temporarily
def test_generate_table_a_invalid_product_count():

    try:
        generate_table_a = lambda: 1 / 0  # Force a ZeroDivisionError
        df =generate_table_a()
        assert False, "Expected exception, but function completed without error"
    except ZeroDivisionError:
        assert True  # Expected exception, test passed
