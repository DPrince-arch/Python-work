def complex_addition(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])

def complex_subtraction(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])

def complex_multiplication(c1, c2):
    return (c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0])

def complex_division(c1, c2):
    denominator = c2[0]**2 + c2[1]**2
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return ((c1[0] * c2[0] + c1[1] * c2[1]) / denominator, (c1[1] * c2[0] - c1[0] * c2[1]) / denominator)
