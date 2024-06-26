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
Library.update_total_books(170)
print(f"Total books after update: {Library.total_books}")