class Book:
    books = []
    def __init__(self, title, author, ISBN, genre, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.quantity = quantity
        Book.books.append(self)
        
    def display_info(self):
        print(f"{self.title} by {self.author} ({self.ISBN}) - {self.genre}, Qty: {self.quantity}")
        
    
    @classmethod
    def total_books(cls):
        return len(cls.books)
    
    @classmethod
    def find_by_title(cls, title):
        return [book for book in cls.books if book.title.lower() ==  title.lower()]
    
    
b1 = Book("a", "me", 12345, "romantic", 100)
b1.display_info()
b2 = Book("b", "mee", 123465, "romantic", 100)

print(Book.total_books())