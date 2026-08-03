class Book:
    def __init__(self, title, author, pages):
        if pages <= 0:
            raise ValueError("The number of pages must be greater than zero.")

        self.title = title
        self.author = author
        self.pages = pages


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book):
        self.books.append(new_book)

    def show_books(self):
        if len(self.books) == 0:
            print("There are no books in the library.")
            return

        print("\n===== LIBRARY BOOKS =====")

        for book in self.books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Pages: {book.pages}")
            print("--------------------------")

    def total_books(self):
        return len(self.books)


library = Library()

while True:
    try:
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        pages = int(input("Enter the number of pages: "))

        book = Book(title, author, pages)

        library.add_book(book)

        continu = input("Do you want to add another book? (y/n): ")

        if continu.lower() == "n":
            break

    except ValueError as error:
        print(error)


print("\n===== LIBRARY =====")
library.show_books()

print(f"\nTotal books in the library: {library.total_books()}")