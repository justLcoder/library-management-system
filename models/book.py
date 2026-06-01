class Book():
    """A class that represents a book"""

    def __init__(self, title, author, publication_year):
        self.book_id = None
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def describe(self):
        """Returns a formatted description of the book."""
        return (
            f"ID: {self.book_id}\n"
            f"Title: {self.title.title()}\n"
            f"Author: {self.author.title()}\n"
            f"Publication Year: {self.publication_year}"
        )
    
    