from models.book import Book
from models.member import Member
from services.library import Library


print("=== LIBRARY MANAGEMENT SYSTEM DEMO ===")

# Start with a fresh library
library = Library(auto_load=False)

print("\n=== ADDING BOOKS ===")

library.add_book(
    Book("The Hobbit", "J.R.R. Tolkien", 1937)
)

library.add_book(
    Book("1984", "George Orwell", 1949)
)

for book in library.all_books():
    print(book)

print("\n=== REGISTERING MEMBERS ===")

library.add_member(
    Member("Alice Johnson")
)

library.add_member(
    Member("Bob Smith")
)

for member in library.all_members():
    print(member)

print("\n=== BORROWING A BOOK ===")

library.borrow_book(1, 1)

print("Available books:")

for book in library.available_books():
    print(book)

print("\n=== RETURNING A BOOK ===")

library.return_book(1, 1)

print("Available books after return:")

for book in library.available_books():
    print(book)

print("\n=== SAVING DATA ===")

library.save_to_file()

print("Library saved successfully.")

print("\n=== LOADING DATA ===")

loaded_library = Library(auto_load=False)
loaded_library.load_from_file()

print("\nBooks loaded:")

for book in loaded_library.all_books():
    print(book)

print("\nMembers loaded:")

for member in loaded_library.all_members():
    print(member)

print("\nLoans loaded:")

for loan in loaded_library.loans:
    print(loan)

print("\n=== DEMO COMPLETE ===")