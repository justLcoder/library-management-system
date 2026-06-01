from models.book import Book
from models.member import Member
from models.library import Library

library = Library()

# Create books
book1 = Book("Harry Potter", "J.K. Rowling", 1997)
book2 = Book("Harry Potter", "J.K. Rowling", 1998)
book3 = Book("The Hobbit", "J.R.R. Tolkien", 1937)

# Create members
member1 = Member("Shahzod Tursinboyev")
member2 = Member("John Doe")

# Register books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register members
library.add_member(member1)
library.add_member(member2)

# Verify IDs
print("=== BOOKS ===")
for book in library.all_books():
    print(book.describe())

print("\n=== MEMBERS ===")
for member in library.all_members():
    print(member.describe())

# Search by title
print("\n=== SEARCH ===")
print(library.find_book("Harry Potter"))

# Borrow a book
print("\n=== BORROW ===")
library.borrow_book(1, 1)

print("Available books:")
for book in library.available_books():
    print(book.title)

# Try borrowing same book again
print("\n=== DOUBLE BORROW ===")
library.borrow_book(2, 1)

# Check member borrowed books
print("\n=== MEMBER 1 BORROWED BOOKS ===")
for book in library.borrowed_books_by_member(member1):
    print(book.title)

# Return book
print("\n=== RETURN ===")
library.return_book(1, 1)

print("Available books after return:")
for book in library.available_books():
    print(book.title)

# Return again (edge case)
print("\n=== INVALID RETURN ===")
library.return_book(1, 1)

# Non-existent member
print("\n=== INVALID MEMBER ===")
library.borrow_book(999, 2)

# Non-existent book
print("\n=== INVALID BOOK ===")
library.borrow_book(1, 999)