class MathUtils:
    def add_numbers(number1,number2):
#This static method adds two numbers and returns the sum
     return number1 + number2
#Call the static method without creating an instance 
sum= MathUtils.add_numbers(5,10)
print(sum)
