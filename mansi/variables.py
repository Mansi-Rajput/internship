#### Task #### 
# Assign values to variables, perform operations with variables, 
# and demonstrate variable reassignment.

#### varible assignment ####
a = 8
b = 2
msg = "Hello Python!"
is_python_fun = True

print("initial values: ")
print(f"a = {a}")
print(f"b = {b}")
print(f"message = {msg}")
print(f"is_python_fun = {is_python_fun}")
print()

#### Operations on variables ####
#arithmetic operations
add = a + b
sub = a - b
mul = a * b
div = a / b

print(f"add: {add}")
print(f"sub: {sub}")
print(f"mul: {mul}")
print(f"div: {div}")
print()

#string operations
msg_upper = msg.upper()
msg_lower = msg.lower()
msg_concat = msg + " " + "Let's have fun!"

print(f"Uppercase: {msg_upper}")
print(f"Lowercase: {msg_lower}")
print(f"msg_concat: {msg_concat}")
print()

#Boolean Operation
bool_and = is_python_fun and (a>b)
bool_or = is_python_fun or (a<b)
bool_not = not is_python_fun

print(f"is_python_fun and (a>b): {bool_and}")
print(f"is_python_fun or (a<b): {bool_or}")
print(f"not is_python_fun: {bool_not}")
print()

#### Reassigning values ####
a = 7
print(f"reassingning a. New value: {a}")

b = 9
print(f"reassingning b. New value: {b}")

msg = "Python is great!"
print(f"message after reassingning: {msg}")

is_python_fun = False
print(f"Reassigning boolean. New value: {is_python_fun}")