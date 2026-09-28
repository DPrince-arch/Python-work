from Modes.central_tendency import mean

def variance(data):
    n = len(data)
    if n == 0:
        raise ValueError("The dataset cannot be empty.")
    
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / n

def standard_deviation(data):
    sd = variance(data) ** 0.5
    return sd

def mean_deviation(data):
    n = len(data)
    if n == 0:
        raise ValueError("The dataset cannot be empty.")
    
    mean = sum(data) / n
    return sum(abs(x - mean) for x in data) / n

def interquartile_range(data):
    n = len(data)
    if n == 0:
        raise ValueError("The dataset cannot be empty.")
    
    data.sort()
    q1 = data[n // 4]
    q3 = data[3 * n // 4]
    return q3 - q1

def coefficient_of_variation(data):
    n = standard_deviation(data) / mean(data)
    return n * 100

def mean_absolute_deviation(data):
    n = len(data)
    if n == 0:
        raise ValueError("The dataset cannot be empty.")
    
    mean = sum(data) / n
    return sum(abs(x - mean) for x in data) / n