"""
Project 0, test_calculator.py. Author: anderpaa@uio.no

This program contains tests for the functions "add()",
"factorial()", "sin()", "divide()", "multiply()", and "cos()"
in "calculator.py".
"""
import math
import pytest
import calculator as calc


# exercise 1:
def test_add_exercise_1():
    """
    Function for testing integer addition with "add()".
    """
    result = calc.add(1, 2)
    assert result == 3


# exercise 2:
def test_float_add_exercise_2():
    """
    Function for testing floating point addition with
    "add()".
    """
    expected = 0.3
    result = calc.add(0.1, 0.2)
    assert math.isclose(expected, result)


# exercise 3:
def test_string_add_exercise_3():
    """
    Function for testing string addition with "add()"
    """
    expected = "Hello World"
    result = calc.add("Hello ", "World")
    assert expected == result


# exercise 4:
def test_factorial_exercise_4():
    """
    Function for testing factorial in calculator.py.
    """
    n = 11
    expected = math.factorial(n)
    result = calc.factorial(n)
    assert expected == result


def test_zero_factorial_exercise_4():
    """
    Function for testing 0! with factorial in calculator.py.
    """
    expected = 1
    result = calc.factorial(0)
    assert expected == result


def test_sin_exercise_4():
    """
    Function for testing sine approximation
    in calculator.py.
    """
    x = math.pi/4
    N = 84

    expected = math.sqrt(1/2)
    result = calc.sin(x, N)
    assert math.isclose(expected, result)


def test_divide_exercise_4():
    """
    Function for testing division in calculator.py.
    """
    x, y = 2, 3
    expected = x/y
    result = calc.divide(x, y)
    assert math.isclose(expected, result)


def test_multiply_exercise_4():
    """
    Function for testing multiplication in calculator.py.
    """
    x, y = 2, 3
    expected = x*y
    result = calc.multiply(x, y)
    assert math.isclose(expected, result)


def test_cos_exercise_4():
    """
    Function for testing cosine approximation in calculator.py.
    """
    x = math.pi/4
    N = 85

    expected = math.sqrt(1/2)
    result = calc.cos(x, N)
    assert math.isclose(expected, result)


# exercise 5:
def test_add_raises_TypeError_for_string_number_addition_exercise_5():
    """
    Function testing if using calculator.add(), with a number and string,
    raises TypeError.
    """
    with pytest.raises(TypeError):
        x = 4
        y = "Dad"
        calc.add(x, y)


def test_divide_raises_ZeroDivisionError_when_dividing_by_zero_exercise_5():
    """
    Function testing if division by zero in calculator.divide() raises
    ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        x, y = 11, 0
        calc.divide(x, y)


# exercise 6:
@pytest.mark.parametrize(
    "arg, expected_output", [[(1, 2), 3], [(4, -2), 2], [(123, -52), 71],
                             [("Beep ", "boop"), "Beep boop"],
                             [("1e-19 ", "9e-19"), "1e-19 9e-19"],
                             [("Big ", "Chungus"), "Big Chungus"]]
)
def test_add_string_and_int_exercise_6(arg, expected_output):
    """
    Function for testing integer addition with "add()".
    """
    assert calc.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(0.1, 0.2), 0.3], [(1e-19, 9e-19), 1e-18],
                             [(7e25, 2.25e22), 7.00225e25]]
)
def test_float_add_exercise_6(arg, expected_output):
    """
    Function for testing floating point addition with
    "add()".
    """
    assert math.isclose(expected_output, calc.add(arg[0], arg[1]))


@pytest.mark.parametrize(
    "arg, expected_output", [(6, math.factorial(6)), (11, math.factorial(11)),
                             (170, math.factorial(170)), (0, 1)]
)
def test_factorial_exercise_6(arg, expected_output):
    """
    Function for testing factorial in calculator.py.
    """
    assert calc.factorial(arg) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(math.pi/4, 10), math.sqrt(1/2)],
                             [(math.pi*5/6, 50), 0.5],
                             [(math.pi*7/3, 20), math.sqrt(3)/2]]
)
def test_sin_exercise_6(arg, expected_output):
    """
    Function for testing sine approximation
    in calculator.py.
    """
    assert math.isclose(expected_output, calc.sin(arg[0], arg[1]))


@pytest.mark.parametrize(
    "arg, expected_output", [[(0.1, 0.2), 0.5], [(1e-19, 9e-19), 1/9],
                             [(7e25, 2.24e22), 3125]]
)
def test_divide_exercise_6(arg, expected_output):
    """
    Function for testing division in calculator.py.
    """
    assert math.isclose(expected_output, calc.divide(arg[0], arg[1]))


@pytest.mark.parametrize(
    "arg, expected_output", [[(0.1, 0.2), 0.02], [(1e-19, 9e-19), 9e-38],
                             [(7e25, 2.24e22), 1.568e48]]
)
def test_multiply_exercise_6(arg, expected_output):
    """
    Function for testing multiplication in calculator.py.
    """
    assert math.isclose(expected_output, calc.multiply(arg[0], arg[1]))


@pytest.mark.parametrize(
    "arg, expected_output", [[(math.pi/4, 10), math.sqrt(1/2)],
                             [(math.pi*5/6, 50), -math.sqrt(3)/2],
                             [(math.pi*7/3, 20), 0.5]]
)
def test_cos_exercise_6(arg, expected_output):
    """
    Function for testing cosine approximation in calculator.py.
    """
    assert math.isclose(expected_output, calc.cos(arg[0], arg[1]))


@pytest.mark.parametrize(
    "arg", [(1, "boop"), ("9e-19", -2), (123, "Big Chungus")]
)
def test_add_raises_TypeError_for_string_number_addition_exercise_6(arg):
    """
    Function testing if using calculator.add(), with a number and string,
    raises TypeError.
    """
    with pytest.raises(TypeError):
        calc.add(arg[0], arg[1])


@pytest.mark.parametrize(
    "arg", [(0.1, 0), (1e-19, 0), (7e25, 0), (0, 0)]
)
def test_divide_raises_ZeroDivisionError_when_dividing_by_zero_exercise_6(arg):
    """
    Function testing if division by zero in calculator.divide() raises
    ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError):
        calc.divide(arg[0], arg[1])
