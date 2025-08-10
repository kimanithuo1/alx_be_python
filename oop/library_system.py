class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # call Book.__init__
        self.file_size = file_size  # in KB


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        # Initialize an empty list to hold Book / EBook / PrintBook instances
        self.books = []

    def add_book(self, book):
        # Optionally check type
        if not isinstance(book, Book):
            raise TypeError("Only Book (or subclasses) instances can be added to the Library")
        self.books.append(book)

    def list_books(self):
        # Print details for each stored book
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")