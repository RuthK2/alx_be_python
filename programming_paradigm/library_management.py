class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def is_available(self):
        return not self._is_checked_out
class Library:
    def __init__(self):
        self._books = []
    def add_book(self,book):
        self._books.append(book)
    def check_out_book(self,title):
        """Marks a book as checked out if it's available."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    return  # checked out successfully
                else:
                    print(f"{book.title} is already checked out.")
                    return
        print(f"{title} not found in the library.")

    def return_book(self, title):
        """Marks a book as returned."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.return_book():
                    return  # returned successfully
                else:
                    print(f"{book.title} was not checked out.")
                    return
        print(f"{title} not found in the library.")

    def list_available_books(self):
        """Displays all available (not checked out) books."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
                 
        