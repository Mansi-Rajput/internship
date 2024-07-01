def sum_all(*args):
   total= 0
for num in args:
    total +=num

result = sum_all(1,2,3,4,5)
print(result)

def print_info(**kwargs):
 for key,value in kwargs.items():
    print(key,value)
