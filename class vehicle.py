class Vehicle:
    count = 0
    def __init__(self, brand):
        self.brand = brand
        Vehicle.count += 1
b1 = raw_input("Enter 1st vehicle brand: ")
b2 = raw_input("Enter 2nd vehicle brand: ")
b3 = raw_input("Enter 3rd vehicle brand: ")
v1 = Vehicle(b1)
v2 = Vehicle(b2)
v3 = Vehicle(b3)
print("Number of Vehicle objects created:", Vehicle.count)
