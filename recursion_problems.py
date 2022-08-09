#  power of numbers 

def power_of_numbers(base, exp):
    assert exp >= 0 and int(exp) == exp, "The exponent must be positive integer"
    if exp == 1: 
        return base
    if exp == 0: 
        return 1
    return base * power_of_numbers(base, exp - 1)

print(power_of_numbers(2, -1))
