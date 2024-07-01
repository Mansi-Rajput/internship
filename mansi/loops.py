#### Challenge ####
# Write a function print_even_numbers that takes a limit as an argument.
# Use a for loop to print all even numbers up to the limit.

def print_even_numbers(limit):
    """Print the numbers that are even from a given limit"""
    for i in range(0, limit + 1):
        if i % 2 == 0:
            print(i)

limit = int(input("Enter your limit for even numbers: "))
print_even_numbers(limit)

#### Challenge ####
# Write another function countdown that takes a starting number as an argument.
# Use a while loop to print a countdown from the starting number to 0.
def countdown(start_num):
    """Count the numbers from the starting number to 0"""
    current_num = start_num

    while current_num >= 0:
        print(current_num)
        current_num -= 1

start_num = int(input("Enter the starting number for countdown: "))
countdown(start_num)