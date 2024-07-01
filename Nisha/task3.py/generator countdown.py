def countdown(n):
    """Generator that counts down from n to 0."""
    while n >= 0:
        yield n
        n -= 1

# countdown generator
if __name__ == "__main__":
    for number in countdown(5):
        print(number)

def countdown(n):
    """Generator that counts down from n to 0."""
    while n >= 0:
        yield n
        n -= 1

# countdown generator
if __name__ == "__main__":
    for number in countdown(10):
        print(number)
