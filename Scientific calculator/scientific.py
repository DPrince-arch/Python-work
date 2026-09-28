import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)


def cube_root(a):
    return math.copysign(abs(a) ** (1 / 3), a)


def factorial(a):
    if a < 0 or int(a) != a:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(int(a))


def natural_log(a):
    if a <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(a)


def log_base_10(a):
    if a <= 0:
        raise ValueError("Log base 10 is only defined for positive numbers.")
    return math.log10(a)


def log_base_n(a, n):
    if a <= 0:
        raise ValueError("Log is only defined for positive numbers.")
    if n <= 0 or n == 1:
        raise ValueError("Log base must be positive and not equal to 1.")
    return math.log(a, n)


def exponential(a):
    return math.exp(a)