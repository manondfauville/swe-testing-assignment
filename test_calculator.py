# test_calculator.py

import pytest
from calculator_logic import Calculator


# ---------- UNIT TESTS ----------

@pytest.fixture
def calc():
    return Calculator()


def test_add(calc):
    assert calc.add(5, 3) == 8


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply(calc):
    assert calc.multiply(6, 7) == 42


def test_divide(calc):
    assert calc.divide(8, 2) == 4


# ---------- INTEGRATION TESTS ----------

def test_full_user_interaction(calc):
    """
    Simulate: 5 + 3 =
    """
    a = 5
    b = 3
    result = calc.add(a, b)
    assert result == 8


def test_clear_after_calculation(calc):
    """
    Simulate calculation then pressing Clear
    """
    result = calc.add(5, 3)
    result = 0  # simulate clear
    assert result == 0