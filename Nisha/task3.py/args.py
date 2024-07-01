def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))  
print(sum_all(20, 30, 40))  
print(sum_all(6, 6, 6, 6, 6))  

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="liza", age=25, city="toronto")
print_info(country="canada", occupation="Network security engineer")
print_info(hobbies=["reading", "writing", "coding"])