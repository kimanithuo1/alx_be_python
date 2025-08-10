class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"{super().__str__()} EBook, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count  # number of pages

    def __str__(self):
        return f"{super().__str__()} PrintBook, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # store Book, EBook, and PrintBook instances

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for idx, book in enumerate(self.books, start=1):
                print(f"{idx}. {book}")