#### Task ####
# Perform arithmetic operations, string manipulations, 
# and boolean comparisons.

#### Integers ####
int_a = 10
int_b = 2

# operations
int_add = int_a + int_b
int_sub = int_a - int_b
int_div = int_a / int_b
int_floor_div = int_a // int_b
int_mul = int_a * int_b
int_mod = int_a % int_b 
int_exp = int_a ** int_b

# Printing Result
print("Integer Operations: ")
print(f"add: {int_add}")
print(f"sub: {int_sub}")
print(f"div: {int_div}")
print(f"floor_div: {int_floor_div}")
print(f"mul: {int_mul}")
print(f"mod: {int_mod}")
print(f"exp: {int_exp}")
print("\n")

#### Float ####
float_a = 7.4
float_b = 5.2

#operaions
float_add = float_a + float_b
float_sub = float_a - float_b
float_mul = float_a * float_b
float_div = float_a / float_b
float_floor_div = float_a // float_b
float_mod = float_a % float_b

#printing result
print("Float Operations: ")
print(f"add: {float_add}")
print(f"sub: {float_sub}")
print(f"f_mul: {float_mul}")
print(f"f_div: {float_div}")
print(f"f_floor_div: {float_floor_div}")
print(f"f_mod: {float_mod}")
print("\n")

#### String ####
str_a = "Hello"
str_b = "World"

#operations
str_concat = str_a +" "+ str_b
str_upper = str_a.upper()
str_lower = str_b.lower()
str_repeat = str_a * 3

#printing result
print("String Operations: ")
print(f"Concatenation: {str_concat}")
print(f"Uppercase: {str_upper}")
print(f"Lowercase: {str_lower}")
print(f"Repeatation: {str_repeat}")
print("\n")

#### Booleans ####
bool_a = True
bool_b = False

#operations
bool_and = bool_a and bool_b 
bool_or = bool_a or bool_b
bool_not_a = not bool_a
bool_equal = int_a == int_b

#printing result
print("Boolean Operations and Comparisons: ")
print(f"{bool_a} and {bool_b} = {bool_and}")
print(f"{bool_a} or {bool_b} = {bool_or}")
print(f"not {bool_a} = {bool_not_a}")
print(f"{int_a} == {float_a} = {bool_equal}")