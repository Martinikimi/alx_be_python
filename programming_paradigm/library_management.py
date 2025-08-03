# programming_paradigm/library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Adds a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks the book with matching title as checked out."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book titled '{title}' not available for checkout.")

    def return_book(self, title):
        """Marks the book with matching title as available again."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book titled '{title}' was not checked out.")

    def list_available_books(self):
        """Prints all books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

