def modulo_remainder(x, y, z):
    # Append the power (x^y)
    x = x**y
    # Floor division to find the nearest integer
    integer = x // z
    # Calculate the remainder
    remainder = x - (integer * z) 
    return remainder

print("Modulo calculation format is: x^y mod z")
x = int(input("Enter x:"))
y = int(input("Enter y:"))
z = int(input("Enter z:"))
print(modulo_remainder(x, y, z))
