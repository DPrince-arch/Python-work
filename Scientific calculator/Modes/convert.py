import math

def conversion(num):
    if num == 1:
        data = int(input("Enter number: "))
        return data * 2.54
    
    elif num == 2:
        data = int(input("Enter number: "))
        return data / 2.54
    
    elif num == 3:
        data = int(input("Enter number: "))
        return data / 3.281
    
    elif num == 4:
        data = int(input("Enter number: "))
        return data * 3.281
    
    elif num == 5:
        data = int(input("Enter number: "))
        return data * 0.9144
    
    elif num == 6:
        data = int(input("Enter number: "))
        return data / 0.9144
    
    elif num == 7:
        data = int(input("Enter number: "))
        return data * 1.60934
    
    elif num == 8:
        data = int(input("Enter number: "))
        return data / 1.60934
    
    elif num == 9:
        data = int(input("Enter number: "))
        return data * 1852
    
    elif num == 10:
        data = int(input("Enter number: "))
        return data / 1852
    
    elif num == 11:
        data = int(input("Enter number: "))
        return data * 4046.86
    
    elif num == 12:
        data = int(input("Enter number: "))
        return data / 4046.86
    
    elif num == 13:
        data = int(input("Enter number: "))
        return data * 3.78541
    
    elif num == 14:
        data = int(input("Enter number: "))
        return data / 3.78541
    
    elif num == 15:
        data = int(input("Enter number: "))
        return data * 4.546
    
    elif num == 16:
        data = int(input("Enter number: "))
        return data / 4.546
    
    elif num == 17:
        data = int(input("Enter number: "))
        return data * (3.086 * math.e) + 13

    elif num == 18:
        data = int(input("Enter number: "))
        return (data - 13) / (3.086 * math.e)   

    elif num == 19:
        data = int(input("Enter number: "))
        return data / 3.6

    elif num == 20:
        data = int(input("Enter number: "))
        return data * 3.6

    elif num == 21:
        data = int(input("Enter number: "))
        return data * 28.3495

    elif num == 22:
        data = int(input("Enter number: "))
        return data / 28.3495

    elif num == 23:
        data = int(input("Enter number: "))
        return data * 0.453592

    elif num == 24:
        data = int(input("Enter number: "))
        return data / 0.453592

    elif num == 25:
        data = int(input("Enter number: "))
        return data * 101325

    elif num == 26:
        data = int(input("Enter number: "))
        return data / 101325

    elif num == 27:
        data = int(input("Enter number: "))
        return data * 133.322

    elif num == 28:
        data = int(input("Enter number: "))
        return data / 133.322

    elif num == 29:
        data = int(input("Enter number: "))
        return data / 1.341
    
    elif num == 30:
        data = int(input("Enter number: "))
        return data * 1.341
    
    elif num == 31:
        data = int(input("Enter number: "))
        return data * 98066.5
    
    elif num == 32:
        data = int(input("Enter number: "))
        return data / 98066.5
    
    elif num == 33:
        data = int(input("Enter number: "))
        return data * 9.80665
    
    elif num == 34:
        data = int(input("Enter number: "))
        return data / 9.80665
    
    elif num == 35:
        data = int(input("Enter number: "))
        return data * 6.89476
    
    elif num == 36:
        data = int(input("Enter number: "))
        return data / 6.89476
    
    elif num == 37:
        data = int(input("Enter number: "))
        return (data - 32) * 5/9
    
    elif num == 38:
        data = int(input("Enter number: "))
        return (data * 9/5) + 32
    
    elif num == 39:
        data = int(input("Enter number: "))
        return data / 4184
    
    elif num == 40:
        data = int(input("Enter number: "))
        return data * 4184
    
    else:
        return "Invalid option. Please select a valid conversion option."