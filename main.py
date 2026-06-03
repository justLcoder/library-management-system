from models.book import Book
from models.member import Member 
from models.loan import Loan 
from models.library import Library 

library = Library()

library.load_from_file()

print(library.books)
print(library.members)
print(library.loans)