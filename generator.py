#### Task ####
#Write a generator function countdown that takes a number and counts down to zero.
#Iterate over the generator and print each number.

def countdown(n):
    """Generator Function to count from a starting number to zero"""
    while n > 0:
        yield n
        n -= 1

#iteration
num = int(input("Enter a starting number: "))
for number in countdown(num):
    print(number)  
