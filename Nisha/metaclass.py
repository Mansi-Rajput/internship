class SingletonMeta(type):
    """
    A metaclass that creates a Singleton base class when called.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SingletonClass(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Testing the Singleton behavior
if __name__ == "__main__":
    s1 = SingletonClass(2)
    s2 = SingletonClass(3)

    print(s1 is s2)  # True
    print(s1.value)  # 2
    print(s2.value)  # 3
