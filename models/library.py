from datetime import date
import json

from .book import Book
from .member import Member
from .loan import Loan


class Library:
    """Represents a library."""

    def __init__(self, books = None, members = None, loans = None):
        self.books = [] if books is None else books
        self.members = [] if members is None else members
        self.loans = [] if loans is None else loans
        self.next_book_id = 1
        self.next_member_id = 1
        self.next_loan_id = 1
    
    def save_to_file(self):
        filename = 'library.json'
        with open(filename, 'w') as f_obj:
            content = {}
            books = []
            members = []
            loans = []
            for book in self.books:
                books.append(book.to_dict())
            content['books'] = books
            for member in self.members:
                members.append(member.to_dict())
            content['members'] = members
            for loan in self.loans:
                loans.append(loan.to_dict())
            content['loans'] = loans
            content['next_book_id'] = self.next_book_id
            content['next_member_id'] = self.next_member_id
            content['next_loan_id'] = self.next_loan_id
            json.dump(content, f_obj, indent=4)
            

    def add_book(self, book):
        """Adds a book to the books collection."""
        if book.book_id is not None:
            return
        book.book_id = self.next_book_id
        self.books.append(book)
        self.next_book_id += 1
    
    def add_member(self, member):
        """Adds a member to the members list."""
        if member.member_id is not None:
            return
        member.member_id = self.next_member_id
        self.members.append(member)
        self.next_member_id += 1
    
    def find_member(self, member_id):
        """Finds the matching member from the members list."""
        for member in self.members:
            if member.member_id == member_id:
                return member
    
    def find_book(self, title):
        """Finds the matching book(s) from the books collection."""
        matchings = []
        for book in self.books:
            if book.title.title() == title.title():
                matchings.append(book)
        return matchings[0] if len(matchings) == 1 else matchings

    def find_book_by_id(self, book_id):
        """Finds the matching book from the books collection."""
        for book in self.books:
            if book.book_id == book_id:
                return book
    
    def is_available(self, book_id):
        """Returns whether the book is available."""
        for loan in self.loans:
            if loan.is_active() and loan.book.book_id == book_id:
                return False
        return True

    def find_active_loan(self, member_id, book_id):
        """Returns a matching active loan."""
        for loan in self.loans:
            if loan.is_active() and loan.member.member_id == member_id and loan.book.book_id == book_id:
                return loan
        return None
    
    def borrow_book(self, member_id, book_id):
        """Creates a loan - the member borrowed the book."""
        member = self.find_member(member_id)
        if member is None:
            print("Member not found.")
            return 
        book = self.find_book_by_id(book_id)
        if book is None:
            print("Book not found.")
            return
        if self.is_available(book_id):
            loan = Loan(member, book, date.today())
            loan.loan_id = self.next_loan_id
            self.loans.append(loan)
            self.next_loan_id += 1
        else:
            print("Book is not available")
            return
    
    def return_book(self, member_id, book_id):
        """Inactivates the matching loan."""
        loan = self.find_active_loan(member_id, book_id)
        if loan is not None:
            loan.returned_date = date.today()
        else:
            print("Loan not found.")
    
    def all_books(self):
        """Returns the book collection."""
        return self.books.copy()
    
    def all_members(self):
        """Returns the list of members."""
        return self.members.copy()
    
    def available_books(self):
        """Returns the list of available books."""
        available_books = []
        for book in self.books:
            if self.is_available(book.book_id):
                available_books.append(book)
        return available_books
    
    def borrowed_books_by_member(self, member):
        """Returns the list of borrowed book by the member."""
        borrowed_books = []
        for book in self.books:
            if self.find_active_loan(member.member_id, book.book_id) is not None:
                borrowed_books.append(book)
        return borrowed_books
    
    def load_from_file(self):
        filename = 'library.json'
        with open(filename) as f_obj:
            data = json.load(f_obj)
            self.next_book_id = data['next_book_id']
            self.next_member_id = data['next_member_id']
            self.next_loan_id = data['next_loan_id']
            for book in data['books']:
                self.books.append(Book.from_dict(book))
            for member in data['members']:
                self.members.append(Member.from_dict(member))
            for loan in data['loans']:
                self.loans.append(Loan(
                                        self.find_member(loan['member_id']), 
                                        self.find_book_by_id(loan['book_id']),
                                        date.fromisoformat(loan['borrowed_date'])
                                        ))
                self.loans[-1].loan_id = loan['loan_id']
                if loan['returned_date'] != 'None':
                    self.loans[-1].returned_date = date.fromisoformat(loan['returned_date'])
    

    
