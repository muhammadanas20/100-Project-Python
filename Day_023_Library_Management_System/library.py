class Book:
    def __init__(self,title):
       self.title = title
       self.borrower = None
    
    def checkout(self,member):
        if self.borrower: return False
        self .borrower = member
        return True
    
    def return_book(self):
        self.borrower = None
        
books = [Book("Python Basics"),Book("Clean Code")]
choice = input("Book title: ").strip()
book = next((item for item in books if item.title == choice), None)
if book and book.checkout("Anas"):
    print(f"Checked out {book.title}.")
else:
    print("book unavailable.")
    