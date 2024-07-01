#Printing even number with for loop
def print_even_numbers(limit):
  for num in range(2, limit + 1, 2):
    print(num)

def countdown(starting_number):
  
  for num in range(starting_number, 0, -1):
    print(num)


print_even_numbers(15)
countdown(5)    
#Printing countdown from start number to zero
def countdown1(start_num):
    while start_num >= 0:
     print(start_num)
    start_num -= 1
countdown(5)

  
