from book import Book

class Borrower:
    all_borrowers = []
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id
        self.borrowed_books = []
        Borrower.all_borrowers.append(self)
        
    def borrow_book(self, book:Book):
        pass
    
    def return_book(title, author, ISBN, genre, quantity):
        pass