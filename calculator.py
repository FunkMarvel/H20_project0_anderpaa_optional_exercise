"""
Project 0, calculator.py. Author: anderpaa@uio.no

This program contains the functions "add()",
"factorial()", "sin()", "divide()", "multiply()", and "cos()".
"""


def add(x, y):
    """
    Function for addition.
    """
    return x + y


def factorial(n):
    """
    Function for calculating the factorial of an integer.
    """
    assert n >= 0, "WARNING: Negative n in calculator.factorial() !"

    if n == 0:
        return 1
    else:
        n_fac = 1
        for i in range(2, n+1):
            n_fac *= i

        return n_fac


def sin(x, N):
    """
    Function for approximating the sine of x, with
    an N-term Taylor-expansion. Default N = 84.
    """
    assert N <= 84, "WARNING: N is too large in calculator.sin() !"

    sin_x = 0
    for i in range(N+1):
        sin_x += (-1)**i * x**(2*i+1)/factorial(2*i+1)

    return sin_x


def divide(x, y):
    """
    Function for calculating the fraction of two numbers.
    """
    return x/y


def multiply(x, y):
    """
    Function for calculating the product of two numbers.
    """
    return x*y


def cos(x, N=10):
    """
    Function for approximating the cosine of x, with
    an N-term Taylor-expansion. Default N = 10.
    """
    assert N <= 85, "WARNING: N is too large in calculator.cos() !"

    cos_x = 0
    for i in range(N+1):
        cos_x += (-1)**i * x**(2*i)/factorial(2*i)

    return cos_x
