import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
q = b**2 - 4*a*c
if (q > 0):
    d = (-b + math.sqrt(q)) / (2*a)
    d1 = (-b - math.sqrt(q)) / (2*a)
    print("Two distinct real roots:")
    print("d =", d)
    print("d1 =", d1)

elif (q == 0):
    d = -b / (2*a)
    print("One real repeated root:")
    print("d =", d)

else:
    d = -b / (2*a)
    d1 = math.sqrt(abs(q)) / (2*a)
    print("Complex roots:")
    print(d,"+j",d1)
    print(d,"-j",d1)
