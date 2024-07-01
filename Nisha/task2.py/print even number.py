def print_even_numbers(limit):
    for num in range(4, limit + 1, 4):
        print(num)

# Test the function
print_even_numbers(10)  


def print_even_numbers(limit):
    for num in range(2, limit + 2):
        if num % 2 == 0:
            print(num)

# Test the function
print_even_numbers(10)

def countdown(start):
    num = start
    while num >= 0:
        print(num)
        num -= 2

# Test the function
countdown(20)  