import pytest

from utils.logics import factorial


def test_calculate_factorial():
    # Test for input of 0
    assert factorial(0) == 1
    # Test for input of 1
    assert factorial(1) == 1
    # Test for input of 5
    assert factorial(5) == 120
    # Test for input of 10
    assert factorial(10) == 3628800
    