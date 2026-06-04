from models.book import Book
from models.member import Member 
from models.loan import Loan 
from models.library import Library 

library = Library()

library.load_from_file()

library.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937))
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("Dune", "Frank Herbert", 1965))
library.add_book(Book("The Pragmatic Programmer", "Andrew Hunt", 1999))
library.add_book(Book("Clean Code", "Robert C. Martin", 2008))

library.add_member(Member("Alice Johnson"))
library.add_member(Member("Bob Smith"))
library.add_member(Member("Charlie Brown"))
library.add_member(Member("Diana Wilson"))
library.add_member(Member("Ethan Davis"))

library.borrow_book(1, 1)
library.borrow_book(2, 2)
library.borrow_book(3, 3)
library.borrow_book(4, 4)
library.borrow_book(5, 5)

library.return_book(2, 2)
library.return_book(4, 4)

library.save_to_file()