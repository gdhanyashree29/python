class Vehicle:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    def display_details(self):
        print("Brand :", self.brand)
        print("Model :", self.model)
        print("Year :", self.year)
        print("Color :", self.color)
vehicle1 = Vehicle("Mahendra", "thor", 2021, "Black")
vehicle2 = Vehicle("Honda", "city", 2023, "white")
vehicle1.display_details()
print()
vehicle2.display_details()
print()
