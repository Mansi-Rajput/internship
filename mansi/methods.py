#### Task 1 ####
# Define a class Book with attributes title and author.
# Create an instance method display_info that prints the book's title and author.
# Instantiate the Book class and call the display_info method.
class Book:
    def __init__(self, title, author):
        """Initializes instance variables"""
        self.title = title
        self.author = author

    def display_info(self):
        """displays information of the book"""
        print(f"The book's title is {self.title} and the author is {self.author}.")

book_obj = Book("Atomic Habits", "James Clear")
book_obj.display_info()

#### Task 2 ####
# Define a class Library with a class attribute total_books.
# Create a class method update_total_books that updates the total_books attribute.
# Call the class method to modify the class attribute.
class Library:
    # class variable or attribute
    total_books = 0

    @classmethod
    def update_total_books(cls, count):
        #'cls' refers to the class itself
        cls.total_books = count

# Modifying the class attribute
print(f"Total books before update: {Library.total_books}")
update = int(input(""))
Library.update_total_books(170)
print(f"Total books after update: {Library.total_books}")

#### Task 3 ####
# define a class MathUtils with a static method add_numbers that takes two numbers and returns their sum.
# Call the static method without creating an instance of the class.
class MathUtils:

    @staticmethod
    def add_numbers(num1, num2):
        """Static method for returning the addtion of two numbers"""
        return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#Calling the static method without creating an instance of the class   
result = MathUtils.add_numbers(num1, num2)

print(f"The sum is {result}")

#### Task 4 ####
# Define a class Person with a private attribute _age.
# Create a property method age with a getter and setter to access and modify the _age attribute.
# Instantiate the Person class, set the age, and print it.
class Person:
    def __init__(self, age):
        """Initializes variables"""
        self.__age = age

    @property
    def age(self):
        """The @property method is the getter method for age attribute"""
        return self.__age
    
    @age.setter
    def age(self, value):
        """Setter method for setting the value of age attribute"""
        if value < 0:
            print("ValueError: Age cannot be negative")
            self.__age = None
        else:
            self.__age = value

# Initial value
person = Person(5)
print(f"Initial Value: {person.age}")

# Setting age using the setter method
person.age = -1
print(f"Updated Value: {person.age}")