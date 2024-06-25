#Task: Convert integers to floats, floats to integers, strings to integers, and vice versa

#Integer to float 
int_num = 10
float_num = 3.5
result = int_num + float_num
print("Integer to float Conversion")
print(f"{int_num} + {float_num} = {result}")
print(f"type: {type(result)}")
print()

#float to integer 
float_num = 11.5
int_num = int(float_num)
print(f"Float to Integer Conversion: {int_num}")
print(f"type: {type(int_num)}")
print()

#String to integer
str_char = "123"
int_char = int(str_char)
print(f"String to integer conversion: {int_char}")
print(f"type: {type(int_char)}")
print()

#integer to string
int_num = 5
str_num = str(int_num)
print(f"Integer to String conversion: {str_num}")
print(f"type: {type(str_num)}")
print()