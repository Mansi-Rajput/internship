#### Task 1 ####
#Task: Create a metaclass SingletonMeta that ensures only 
# one instance of a class can be created.
class SingletonMeta(type):
    """
    A Singleton metaclass that ensures only one 
    instance of a class is created.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """The __call__ method is responsible for instance creation."""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# 'SingletonClass' uses 'SingletonMeta' as its metaclass
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Creating instances
instance1 = SingletonClass(1)
instance2 = SingletonClass(2)

# Checking if both instances are the same
print(f"Are instance1 and instance2 same? {instance1 is instance2}")
print(f"The value of instance 1: {instance1.value}")         
print(f"The value of instance 2: {instance2.value}")         

#### Task 2 ####
# Create an abstract base class Shape with abstract methods area() 
# and perimeter(), and implement concrete subclasses Circle and Rectangle.
from abc import ABC
import math
class Shape(ABC):
    """abstract class"""

    def area():
        """abstract method"""
        pass

    def perimeter():
        """abstract method"""
        pass

class Circle(Shape):
    """Calculates the area and perimeter of the circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    """Calculates the area and perimeter of the rectangle"""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

#Printing the results 
radius = int(input("Enter the radius of the circle: "))
circle_obj = Circle(radius)
circle_area = circle_obj.area()
circle_perimeter = circle_obj.perimeter()
print(f"Area of circle is {round(circle_area, 2)}")
print(f"Perimeter of circle is {round(circle_perimeter, 2)}")

#Printing the results
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
rect_obj = Rectangle(length, width)
print(f"Area of the rectangle: {rect_obj.area()}")
print(f"Perimeter of the rectangle: {rect_obj.perimeter()}")