class Loan:
    """Represents a library loan - a member borrowing a book."""
    
    def __init__(self, member, book, borrowed_date):
        self.loan_id = None
        self.member = member
        self.book = book
        self.borrowed_date = borrowed_date
        self.returned_date = None
    
    def is_active(self):
        """Return whether the loan is active or not."""
        return self.returned_date is None
    
    def __str__(self):
        return (
            f"Loan #{self.loan_id} | "
            f"{self.member.full_name} -> "
            f"{self.book.title}"

        )