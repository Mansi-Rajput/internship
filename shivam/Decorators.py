import time
from functools import wraps

def time_decorator(func):
    """Decorator to measure the time taken by a function to execute."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("Function",func.__name__,"took execution_time:.f2: seconds to execute.")
        return result
    return wrapper

@time_decorator
def slow_function():
    """A function that sleeps for 2 seconds and then prints "Function complete"."""
    time.sleep(2)
    print("Function complete")

slow_function()
