def linear_equation(a, b):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")
    return -b / a

def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        raise ValueError("The equation has no real roots.")
    
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    
    return root1, root2

def cubic_equation(a, b, c, d):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero.")
    
    b /= a
    c /= a
    d /= a
    
    delta0 = b ** 2 - 3 * c
    delta1 = 2 * b ** 3 - 9 * b * c + 27 * d
    
    discriminant = (delta1 ** 2 - 4 * delta0 ** 3) / -27
    
    if discriminant < 0:
        raise ValueError("The equation has no real roots.")
    
    C = ((delta1 + discriminant ** 0.5) / 2) ** (1/3)
    
    root1 = -1/(3*a) * (b + C + delta0 / C)
    root2 = -1/(3*a) * (b + (-1 + complex(0, 3)**0.5) * C / 2 + delta0 / ((-1 + complex(0, 3)**0.5) * C))
    root3 = -1/(3*a) * (b + (-1 - complex(0, 3)**0.5) * C / 2 + delta0 / ((-1 - complex(0, 3)**0.5) * C))
    
    return root1, root2, root3