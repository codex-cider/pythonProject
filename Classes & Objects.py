# Classes & Objects

print("************ Classes And Object ***************")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("Abhay", 20)

p2 = Person("Ajay", 25)

print(p1.name)
print(p1.age)
