
#list of squares from 1 to 10
squares = [x ** 2 for x in range(1, 11)]
print(squares)

#list of even numbers form 1 to 20
even = [x for x in range(1, 21) if x % 2 == 0]
print(even)

def greet(name):
    print(f"Hello {name}! Have a great day!")

name = input("What's your name?\n")
greet(name)

def calculate_area(length, width):
    print(f"The area of the rectangle is {length * width}")

length = int(input("Enter length of the rectangle: "))
width = int(input("Enter width of the rectangle: "))
calculate_area(length, width)