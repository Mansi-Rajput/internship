# #list of squares from 1 to 10
# squares = [x ** 2 for x in range(1, 11)]
# print(squares)

# #list of even numbers form 1 to 20
# even = [x for x in range(1, 21) if x % 2 == 0]
# print(even)

# #Define a function greet that takes a name as an argument and prints a greeting message.
# def greet(name):
#     """Prints a greeting message with the name given"""
#     print(f"Hello {name}! Have a great day!")

# name = input("What's your name?\n")
# greet(name)

# #Define a function calculate_area that takes length and width as arguments and returns the area of a rectangle.
# def calculate_area(length, width):
#     """prints the area of the rectangle by calculating it"""
#     print(f"The area of the rectangle is {length * width}")

# length = int(input("Enter length of the rectangle: "))
# width = int(input("Enter width of the rectangle: "))
# calculate_area(length, width)

# #Create a lambda function to add two numbers and assign it to a variable add.
# #Use the lambda function to add two numbers and print the result.
# add = lambda a, b: a + b #lambda function
# result = add(5, 10)
# print(f"The addition of the given numbers is: {result}")

#Task: Define a function sum_all that takes any number of arguments 
#and returns their sum using *args.
def sum_all(*args):
    return sum(args)

result1 = sum_all(0, 2, 4, 6, 8, 10)
result2 = sum_all(1, 3, 5, 7, 9)
result3 = sum_all()

print("Positional Arguments (args):")
print(f"The sum of even numbers is: {result1}")
print(f"The sum of odd numbers is: {result2}")
print(f"The sum of no argument is: {result3}")
print()

#Task: Define a function print_info that takes any number 
#of keyword arguments and prints them using **kwargs.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Keyword Arguments (kwargs): ")
print_info(name = "James Henderson", age = 30, city = "New York")
