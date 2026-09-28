def base_conversion(number, from_base, to_base):
    if from_base < 2 or from_base > 36:
        raise ValueError("from_base must be between 2 and 36.")
    if to_base < 2 or to_base > 36:
        raise ValueError("to_base must be between 2 and 36.")

    decimal_value = int(str(number), from_base)

    if decimal_value == 0:
        return '0'

    digits = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        if remainder < 10:
            digits.append(str(remainder))
        else:
            digits.append(chr(remainder - 10 + ord('A')))
        decimal_value //= to_base

    return ''.join(reversed(digits))