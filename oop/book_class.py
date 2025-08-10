class Book:

    """A simple Book class demonstrating magic methods.

    Attributes:
        title (str): book title
        author (str): book author
        year (int): publication year
    """
    def __init__(self, title:str, author:str, year:int):

             # Constructor: initialize attributes

        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        # Human-readable string representation of the book used by print()
        
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        # official string representation of the book
        
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        # Triggered when a book instance is deleted
        print(f"Deleting '{self.title}'")
              
