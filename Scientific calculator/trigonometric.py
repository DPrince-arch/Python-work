import math

def sin_deg(a):
    return math.sin(math.radians(a))


def cos_deg(a):
    return math.cos(math.radians(a))


def tan_deg(a):
    return math.tan(math.radians(a))


def asin_deg(a):
    if not -1 <= a <= 1:
        raise ValueError("asin is only defined for values between -1 and 1.")
    return math.degrees(math.asin(a))


def acos_deg(a):
    if not -1 <= a <= 1:
        raise ValueError("acos is only defined for values between -1 and 1.")
    return math.degrees(math.acos(a))


def atan_deg(a):
    return math.degrees(math.atan(a))