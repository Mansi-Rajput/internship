#### TASK ####
# Write a decorator time_decorator that measures the time taken by a function to execute.
# Use the decorator on a function slow_function that sleeps for 2 seconds and then prints "Function complete".

import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        """This function will execute inside the main function"""
        start_time = time.time() #calculating the start time
        func(*args, **kwargs) #calling the function to execute
        end_time = time.time() #calculating the end time
        exec_time = end_time - start_time #calculating execution time
        print(f"Time taken by {func.__name__} to execute: {exec_time:.4f} seconds")
    return wrapper

#decorating the function
@time_decorator
def slow_func():
    """This is the decorated function"""
    time.sleep(2)
    print("Function completed executing.")

#calling the decorated function
slow_func()