#### TASK ####
# Description: Implement a class decorator to log method calls within a class.
# Task: Create a decorator log_methods that logs the entry and exit of every method call within a class.

#### Note ####
# Logging is a means of tracking events that happen when some software runs. 
# The software’s developer adds logging calls to their code to indicate that certain events have occurred. 
# An event is described by a descriptive message which can optionally contain variable data 
# (i.e. data that is potentially different for each occurrence of the event). 
# Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.
import functools
import logging

# Setting level for configuration
logging.basicConfig(level=logging.INFO)

def log_methods(cls):
    """Class decorator to log method calls within a class"""
    for name, func in cls.__dict__.items():
        if callable(func):
            setattr(cls, name, log_method_calls(func))
    return cls

def log_method_calls(func):
    """A function decorator that logs method calls"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.info(f"Entering: {func.__name__} with args = {args} and kwargs = {kwargs}")
        result = func(self, *args, **kwargs)
        logging.info(f"Exiting: {func.__name__} with result = {result}")
        return result
    return wrapper

@log_methods
class Calculator():
    def add(self, a, b):
        return a + b
    
    def square(self, x):
        return x ** 2
    
calc = Calculator()
calc.add(5, 3)
calc.square(6)