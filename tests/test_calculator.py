"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException

def calc():
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        calc = Calculator()
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self):
        calc = Calculator()
        assert calc.add(-5, -3) == -8

    def test_add_positive_and_negative(self):
        calc = Calculator()
        assert calc.add(5, -3) == 2

    def test_add_negative_and_positive(self):
        calc = Calculator()
        assert calc.add(-5, 3) == -2

    def test_add_with_zero(self):
        calc = Calculator()
        assert calc.add(5, 0) == 5
        assert calc.add(0, 5) == 5

    def test_add_floats(self):
        calc = Calculator()
        assert calc.add(2.5, 3.7) == pytest.approx(6.2)
    
    def test_add_out_of_range(self):
     calc = Calculator()
     with pytest.raises(InvalidInputException):
        calc.add(1000000, 1)
     with pytest.raises(InvalidInputException):
        calc.add(1, 1000000)



class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        calc = Calculator()
        assert calc.subtract(-5, -3) == -2

    def test_subtract_positive_and_negative(self):
        calc = Calculator()
        assert calc.subtract(5, -3) == 8

    def test_subtract_negative_and_positive(self):
        calc = Calculator()
        assert calc.subtract(-5, 3) == -8

    def test_subtract_with_zero(self):
        calc = Calculator()
        assert calc.subtract(5, 0) == 5
        assert calc.subtract(0, 5) == -5

    def test_subtract_floats(self):
        calc = Calculator()
        assert calc.subtract(2.5, 3.7) == pytest.approx(-1.2)
    
    def test_subtract_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
          calc.subtract(1000000, 1)
        with pytest.raises(InvalidInputException):
          calc.subtract(1, 1000000)



class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        calc = Calculator()
        assert calc.multiply(5, 3) == 15

    def test_multiply_negative_numbers(self):
        calc = Calculator()
        assert calc.multiply(-5, -3) == 15

    def test_multiply_positive_and_negative(self):
        calc = Calculator()
        assert calc.multiply(5, -3) == -15

    def test_multiply_negative_and_positive(self):
        calc = Calculator()
        assert calc.multiply(-5, 3) == -15

    def test_multiply_with_zero(self):
        calc = Calculator()
        assert calc.multiply(5, 0) == 0
        assert calc.multiply(0, 5) == 0

    def test_multiply_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1000000, 1)
        with pytest.raises(InvalidInputException):
            calc.multiply(1, 1000000)



class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        calc = Calculator()
        assert calc.divide(6, 3) == 2

    def test_divide_negative_numbers(self):
        calc = Calculator()
        assert calc.divide(-6, -3) == 2

    def test_divide_positive_and_negative(self):
        calc = Calculator()
        assert calc.divide(6, -3) == -2

    def test_divide_negative_and_positive(self):
        calc = Calculator()
        assert calc.divide(-6, 3) == -2

    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(5, 0)

    def test_divide_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
                calc.divide(1000000, 1)
        with pytest.raises(InvalidInputException):
                calc.divide(1, 1000000)

    def test_divide_any_zero_denominator_raises(self):
         calc = Calculator()
         with pytest.raises(Exception):  # ValueError に限定しない
            calc.divide(10, 0)
    
    def test_divide_out_of_range_inputs(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
         calc.divide(1000000, 1)

        with pytest.raises(InvalidInputException):
            calc.divide(1, 1000000)

        with pytest.raises(InvalidInputException):
             calc.divide(-1000000, 2)

        with pytest.raises(InvalidInputException):
            calc.divide(2, -1000000)



class TestCalculateAndValidation:
    """Tests calculate() and input validation."""

    def test_calculate_valid(self):
        calc = Calculator()
        assert calc.calculate(10) == 20

    def test_out_of_range(self):
        calc = Calculator()

        with pytest.raises(InvalidInputException):
            calc.calculate(1000000)

        with pytest.raises(InvalidInputException):
            calc.calculate(-1000000)
    
