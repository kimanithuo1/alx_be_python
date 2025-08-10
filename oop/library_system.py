class Book:
    total_books = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.total_books += 1

    @classmethod
    def display_total_books(cls):
        return f"Total books: {cls.total_books}"

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class PrintBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        return f"Print Book: '{self.title}' by {self.author} ({self.year}), {self.pages} pages"


class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return f"E-Book: '{self.title}' by {self.author} ({self.year}), {self.file_size}MB"
