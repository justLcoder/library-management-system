class Book:
    """Represents a book"""

    def __init__(self, title, author, publication_year):
        self.book_id = None
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def describe(self):
        """Returns a formatted description of the book."""
        return (
            f"ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Publication Year: {self.publication_year}"
        )
    
    def __str__(self):
        return f"{self.book_id}: {self.title}"
    