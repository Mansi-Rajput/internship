import time
from functools import wraps

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

@time_decorator
def example_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

result = example_function(10000)
print(f"Result: {result}")

import time
from functools import wraps

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} executed in {elapsed_time:.4f} seconds")
        return result
    return wrapper

@time_decorator
def slow_function():
    time.sleep(2)
    print("Function complete")

# Call the decorated function
slow_function()

