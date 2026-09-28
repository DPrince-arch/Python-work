import Modes.Bases.binary as binary
import Modes.Bases.hexadecimal as hexadecimal

def decimal_to_octal(number):
    if number < 0:
        raise ValueError("Number must be non-negative.")
    return oct(number)[2:]

def octal_to_decimal(octal_str):
    if not all(digit in '01234567' for digit in octal_str):
        raise ValueError("Input must be an octal string.")
    return int(octal_str, 8)

def octal_to_binary(octal_str):
    decimal_value = octal_to_decimal(octal_str)
    return binary.decimal_to_binary(decimal_value)

def octal_to_hexadecimal(octal_str):
    decimal_value = octal_to_decimal(octal_str)
    return hexadecimal.decimal_to_hexadecimal(decimal_value)

def octal_addition(oct1, oct2):
    decimal_sum = octal_to_decimal(oct1) + octal_to_decimal(oct2)
    return decimal_to_octal(decimal_sum)

def octal_subtraction(oct1, oct2):
    decimal_diff = octal_to_decimal(oct1) - octal_to_decimal(oct2)
    if decimal_diff < 0:
        raise ValueError("Result of subtraction is negative.")
    return decimal_to_octal(decimal_diff)

def octal_multiplication(oct1, oct2):
    decimal_product = octal_to_decimal(oct1) * octal_to_decimal(oct2)
    return decimal_to_octal(decimal_product)

def octal_division(oct1, oct2):
    decimal_dividend = octal_to_decimal(oct1)
    decimal_divisor = octal_to_decimal(oct2)
    if decimal_divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    decimal_quotient = decimal_dividend // decimal_divisor
    return decimal_to_octal(decimal_quotient)

def octal_modulus(oct1, oct2):
    decimal_dividend = octal_to_decimal(oct1)
    decimal_divisor = octal_to_decimal(oct2)
    if decimal_divisor == 0:
        raise ValueError("Modulus by zero is not allowed.")
    decimal_remainder = decimal_dividend % decimal_divisor
    return decimal_to_octal(decimal_remainder)

def octal_power(oct1, oct2):
    decimal_base = octal_to_decimal(oct1)
    decimal_exponent = octal_to_decimal(oct2)
    decimal_result = decimal_base ** decimal_exponent
    return decimal_to_octal(decimal_result)