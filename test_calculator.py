import pytest
from calculator_logic import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ------------------
# NORMAL CASES
# ------------------

def test_add(calc):
    assert calc.add(5, 3) == 8


def test_subtract(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply(calc):
    assert calc.multiply(6, 7) == 42


def test_divide(calc):
    assert calc.divide(8, 2) == 4


# ------------------
# EDGE CASES
# ------------------

# Division by zero
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


# Very large numbers (float overflow)
def test_large_number_multiplication(calc):
    result = calc.multiply(1e308, 10)
    assert result == float("inf")


# Very small numbers
def test_small_decimal_division(calc):
    result = calc.divide(0.0001, 0.1)
    assert result == 0.001


# Negative numbers
def test_negative_numbers(calc):
    assert calc.add(-5, -3) == -8


# Mixed positive and negative
def test_mixed_sign(calc):
    assert calc.subtract(5, -3) == 8


# Decimal numbers
def test_decimal_addition(calc):
    assert calc.add(2.5, 3.7) == pytest.approx(6.2)


# Invalid type input
def test_invalid_type(calc):
    with pytest.raises(TypeError):
        calc.add("5", 3)


# None input
def test_none_input(calc):
    with pytest.raises(TypeError):
        calc.multiply(None, 5)
