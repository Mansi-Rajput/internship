
def greet(name: str) -> str:
    "Return a greeting message with the given name"""
    return "Hello, {keeya}!"

message = greet("keeya")
print(message)  

message = greet("sharma")
print(message)  


def calculate_area(length, width):
    return length * width

length = 10
width = 15
area = calculate_area(length, width)
print(f"The area of the rectangle is {area}")

