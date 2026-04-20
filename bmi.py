def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
def get_bmi_result(self):
        height_m = self.height * 0.3048
        bmi = self.weight / (height_m ** 2)
        if bmi < 18.5:
            return "Under weight"
        elif bmi < 25:
            return "Healthy"
        else:
            return "Obese"
name = raw_input("Enter name: ")
age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (feet): "))
p1 = Person(name, age, weight, height)
print("BMI Result:", p1.get_bmi_result())
