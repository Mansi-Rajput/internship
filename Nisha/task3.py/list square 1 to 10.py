# Create a list of squares of numbers from 1 to 10 using a list comprehension
squares = [i**2 for i in range(1, 11)]

# Print the list of squares
print(squares)

# Create a list of numbers from 1 to 20
numbers = list(range(1, 20))

# Use a list comprehension to filter out even numbers
odd_numbers = [num for num in numbers if num % 2!= 0]

# Print the list of odd numbers
print("Odd numbers:", odd_numbers)