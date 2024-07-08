from abc import ABC, abstractmethod
import math
"""Abstract method to calculate the area of the shape"""
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
"""Abstract method to calculate the perimeter of the shape"""
@abstractmethod
def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius =radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 *math.pi *self.radius

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage:
circle = Circle(5)
print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}")
