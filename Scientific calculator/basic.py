import math

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a / b


def power(a, b):
    return math.pow(a, b)


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Modulus by zero is undefined.")
    return math.fmod(a, b)