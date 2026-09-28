import Modes.Bases.binary as binary
import Modes.Bases.octal as octal

def decimal_to_hexadecimal(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    return hex(number)[2:]

def hexadecimal_to_decimal(hexadecimal_str):
    if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
        raise ValueError("Input must be a hexadecimal string.")
    return int(hexadecimal_str, 16)

def hexadecimal_to_binary(hexadecimal_str):
    decimal_value = hexadecimal_to_decimal(hexadecimal_str)
    return binary.decimal_to_binary(decimal_value)

def hexadecimal_to_octal(hexadecimal_str):
    decimal_value = hexadecimal_to_decimal(hexadecimal_str)
    return octal.decimal_to_octal(decimal_value)

def hexadecimal_addition(hex1, hex2):
    decimal_sum = hexadecimal_to_decimal(hex1) + hexadecimal_to_decimal(hex2)
    return decimal_to_hexadecimal(decimal_sum)

def hexadecimal_subtraction(hex1, hex2):
    decimal_diff = hexadecimal_to_decimal(hex1) - hexadecimal_to_decimal(hex2)
    if decimal_diff < 0:
        raise ValueError("Result of subtraction is negative.")
    return decimal_to_hexadecimal(decimal_diff)

def hexadecimal_multiplication(hex1, hex2):
    decimal_product = hexadecimal_to_decimal(hex1) * hexadecimal_to_decimal(hex2)
    return decimal_to_hexadecimal(decimal_product)

def hexadecimal_division(hex1, hex2):
    decimal_dividend = hexadecimal_to_decimal(hex1)
    decimal_divisor = hexadecimal_to_decimal(hex2)
    if decimal_divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    decimal_quotient = decimal_dividend // decimal_divisor
    return decimal_to_hexadecimal(decimal_quotient)

def hexadecimal_modulus(hex1, hex2):
    decimal_dividend = hexadecimal_to_decimal(hex1)
    decimal_divisor = hexadecimal_to_decimal(hex2)
    if decimal_divisor == 0:
        raise ValueError("Modulus by zero is not allowed.")
    decimal_remainder = decimal_dividend % decimal_divisor
    return decimal_to_hexadecimal(decimal_remainder)

def hexadecimal_power(hex1, hex2):
    decimal_base = hexadecimal_to_decimal(hex1)
    decimal_exponent = hexadecimal_to_decimal(hex2)
    decimal_result = decimal_base ** decimal_exponent
    return decimal_to_hexadecimal(decimal_result)