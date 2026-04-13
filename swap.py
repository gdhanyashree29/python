a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap:", a, b)

a = a + b
b = a - b
a = a - b

print("After swap:", a, b)
