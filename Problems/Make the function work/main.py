def closest_higher_mod_5(x):
    remainder = x % 5
    subtract = 5 - remainder
    if remainder == 0:
        return x
    return x + subtract
