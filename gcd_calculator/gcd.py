# gcd.py

def gcd_two_numbers(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_numbers(numbers):
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required to calculate the GCD.")
    
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd_two_numbers(result, numbers[i])
    
    return result