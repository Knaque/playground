class Person:
    def __init__(self, name, age, height, eye_color, hair_color):
        self.name = name
        self.age = age
        self.height = height
        self.eye_color = eye_color
        self.hair_color = hair_color

p1 = Person("Reilly", 15, "5'10\"", "Green", "Brown")
p2 = Person("Delight", 14, "3'1\"", "Brown", "Black")

print(p1.name)
print(p1.age) 
print(p1.height)
print(p1.eye_color)
print(p1.hair_color)

print("")

print(p2.name)
print(p2.age)
print(p2.height)
print(p2.eye_color)
print(p2.hair_color)
