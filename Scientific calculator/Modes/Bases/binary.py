import math
import Modes.Bases.octal as octal
import Modes.Bases.hexadecimal as hexadecimal


def decimal_to_binary(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    return bin(number)[2:]


def binary_to_decimal(binary_str):
    if not all(bit in "01" for bit in binary_str):
        raise ValueError("Input must be a binary string.")
    return int(binary_str, 2)


def binary_to_octal(binary_str):
    decimal_value = binary_to_decimal(binary_str)
    return octal.decimal_to_octal(decimal_value)


def binary_to_hexadecimal(binary_str):
    decimal_value = binary_to_decimal(binary_str)
    return hexadecimal.decimal_to_hexadecimal(decimal_value)


def binary_addition(bin1, bin2):
    decimal_sum = binary_to_decimal(bin1) + binary_to_decimal(bin2)
    return decimal_to_binary(decimal_sum)


def binary_subtraction(bin1, bin2):
    decimal_diff = binary_to_decimal(bin1) - binary_to_decimal(bin2)
    if decimal_diff < 0:
        raise ValueError("Result of subtraction is negative.")
    return decimal_to_binary(decimal_diff)


def binary_multiplication(bin1, bin2):
    decimal_product = binary_to_decimal(bin1) * binary_to_decimal(bin2)
    return decimal_to_binary(decimal_product)


def binary_division(bin1, bin2):
    decimal_dividend = binary_to_decimal(bin1)
    decimal_divisor = binary_to_decimal(bin2)
    if decimal_divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    decimal_quotient = decimal_dividend // decimal_divisor
    return decimal_to_binary(decimal_quotient)


def binary_modulus(bin1, bin2):
    decimal_dividend = binary_to_decimal(bin1)
    decimal_divisor = binary_to_decimal(bin2)
    if decimal_divisor == 0:
        raise ValueError("Modulus by zero is not allowed.")
    decimal_remainder = decimal_dividend % decimal_divisor
    return decimal_to_binary(decimal_remainder)


def binary_power(bin1, bin2):
    decimal_base = binary_to_decimal(bin1)
    decimal_exponent = binary_to_decimal(bin2)
    decimal_result = decimal_base ** decimal_exponent
    return decimal_to_binary(decimal_result)