class Person:
    def __init__(self, name):
        self.name =name
        self._age = 0 #Private attribute for age
    @property
    def age(self):
        return self.age

    def age(self, new_age):
        if age >= 0:
            self._age = new_age
        else:
            print("Age cannot be negative.setting age to 0.")
            self.age =0
name= input("Enter your name:")
age = int(input("Enter your age here:"))

person1= Person(name)
person1.age = age
print(person1.name,"is",person1.age,"Year old.")
