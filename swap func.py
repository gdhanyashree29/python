def swap(a, b):
    a, b = b, a
    return a, b

x = int(input("Enter first value: "))
y = int(input("Enter second value: "))

x, y = swap(x, y)
print("After swapping:")
print("x =", x)
print("y =", y)
