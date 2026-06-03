class Book:
    """Represents a book"""

    def __init__(self, title, author, publication_year):
        self.book_id = None
        self.title = title
        self.author = author
        self.publication_year = publication_year

    # Serializer and deserializer:
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'publication_year': self.publication_year
        }
    
    @classmethod
    def from_dict(cls, data):
        book = cls(
            data['title'],
            data['author'],
            data['publication_year']
        )
        book.book_id = data['book_id']
        return book
    

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
    