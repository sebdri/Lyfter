def add_book():
    book_name = input("Please enter the name of the book: ")
    book_author = input("Please enter the author's name: ")

    while True:
        try:
            book_year = int(input("Add the publication year: "))

            if book_year > 0:
                break
            else:
                print("Year must be greater than 0.")

        except ValueError:
            print("Invalid data.")

    books_category = input("Add the category of your book: ")

    while True:
        available = input("Is the book available? (YES/NO): ").strip().lower()

        if available == "yes" or available == "no":
            break
        else:
            print("Please enter only YES or NO.")

    book = {
        "Name": book_name,
        "Author": book_author,
        "Year": book_year,
        "Category": books_category,
        "Availability": available
    }

    return book


def View_Books(books):

    if len(books) == 0:
        print("You need to add a book first.")
        return

    for book in books:

        print(f"Name: {book['Name']}")
        print(f"Author: {book['Author']}")
        print(f"Year: {book['Year']}")
        print(f"Category: {book['Category']}")
        print(f"Availability: {book['Availability']}")
        print("-" * 30)


def show_available_books(books):

    if len(books) == 0:
        print("No books added.")
        return

    found = False

    for book in books:

        if book["Availability"] == "yes":

            found = True

            print(f"Name: {book['Name']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}")
            print(f"Category: {book['Category']}")
            print(f"Availability: {book['Availability']}")
            print("-" * 30)

    if not found:
        print("No available books.")


def search_book(books):

    if len(books) == 0:
        print("No books added.")
        return

    user_book = input("Please enter the name of the book: ").strip().lower()

    found = False

    for book in books:

        if user_book == book["Name"].lower():

            found = True

            print(f"Name: {book['Name']}")
            print(f"Author: {book['Author']}")
            print(f"Year: {book['Year']}")
            print(f"Category: {book['Category']}")
            print(f"Availability: {book['Availability']}")
            print("-" * 30)

    if not found:
        print("Book not found.")