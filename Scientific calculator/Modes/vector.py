import math

def vector_addition(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions for addition.")
    return [v1[i] + v2[i] for i in range(len(v1))]

def vector_subtraction(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions for subtraction.")
    return [v1[i] - v2[i] for i in range(len(v1))]

def vector_dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimensions for dot product.")
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def vector_cross_product(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("Cross product is only defined for 3-dimensional vectors.")
    return [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]

def vector_magnitude(v):
    return sum(x ** 2 for x in v) ** 0.5

def vector_normalization(v):
    magnitude = vector_magnitude(v)
    if magnitude == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return [x / magnitude for x in v]

def vector_angle(v1, v2):
    dot_product = vector_dot_product(v1, v2)
    magnitude_v1 = vector_magnitude(v1)
    magnitude_v2 = vector_magnitude(v2)
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        raise ValueError("Cannot calculate angle with the zero vector.")
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    return math.acos(cos_theta)

def vector_projection(v1, v2):
    dot_product = vector_dot_product(v1, v2)
    magnitude_v2_squared = vector_magnitude(v2) ** 2
    if magnitude_v2_squared == 0:
        raise ValueError("Cannot project onto the zero vector.")
    scalar_projection = dot_product / magnitude_v2_squared
    return [scalar_projection * x for x in v2]
