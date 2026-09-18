# Simple Library System
# This project shows basic OOP in Python.
# We use classes, objects, variables, and functions only.


class Book:
    # A book has a name, author, and a status that tells if it is available.
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Member:
    # A member has a name and a list of books they borrowed.
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    # The library keeps all books and members.
    def __init__(self):
        self.books = []
        self.members = []

    # Add a book to the library.
    def add_book(self, book):
        self.books.append(book)

    # Add a member to the library.
    def add_member(self, member):
        self.members.append(member)

    # Borrow a book by title.
    def borrow_book(self, title, member):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.available = False
                    member.borrowed_books.append(book)
                    print(member.name, "borrowed", book.title)
                    return
                else:
                    print("Book is already borrowed.")
                    return

        print("Book not found.")

    # Return a book to the library.
    def return_book(self, title, member):
        for book in member.borrowed_books:
            if book.title == title:
                book.available = True
                member.borrowed_books.remove(book)
                print(member.name, "returned", book.title)
                return

        print("This book was not borrowed by this member.")

    # Show the book list and their status.
    def display_books(self):
        print("\nLibrary Books:")

        for book in self.books:
            if book.available:
                status = "Available"
            else:
                status = "Borrowed"

            print(book.title, "-", book.author, "-", status)


# Create the library object.
library = Library()

# Create book objects.
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("The Lion King", "Roger Allers")

# Add books to the library.
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create a member object.
member1 = Member("Faisal")

# Add the member to the library.
library.add_member(member1)

# Show all books.
library.display_books()

# Borrow a book.
library.borrow_book("Harry Potter", member1)

# Show books after borrowing.
library.display_books()

# Return the borrowed book.
library.return_book("Harry Potter", member1)

# Show books after returning.
library.display_books()