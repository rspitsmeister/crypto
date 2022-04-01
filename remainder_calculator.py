def modulo_remainder(x, y, z):
    # Append the power (x^y)
    x = x**y
    # Floor division to find the nearest integer
    integer = x // z
    # Calculate the remainder
    remainder = x - (integer * z) 
    return remainder

print(modulo_remainder(3, 95, 673))
print(modulo_remainder(3, 240, 673))
print(modulo_remainder(529, 95, 673))
print(modulo_remainder(525, 240, 673))