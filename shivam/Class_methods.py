class Library:
  total_books = 0  # Class attribute to store total books

  @classmethod
  def update_total_books(cls, new_books):
    cls.total_books += new_books
Library.update_total_books(23)  # Add 23 books
print("Total books in the library: ",Library.total_books)
