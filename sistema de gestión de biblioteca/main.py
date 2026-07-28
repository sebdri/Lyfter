from menu import menu
from Books_data import add_book, View_Books, show_available_books, search_book
from data_transfer import export_data, import_data


def main():
    books = []

    while True:
        option = menu()

        if option == 1:
            book = add_book()
            books.append(book)
            print("\nBook successfully added.\n")

        elif option == 2:
            print("\n===== Library Books =====")
            View_Books(books)

        elif option == 3:
            search_book(books)

        elif option == 4:
            print("\n===== Available Books =====")
            show_available_books(books)

        elif option == 5:
            export_data("books.csv", books)

        elif option == 6:
            books = import_data("books.csv", books)

        elif option == 7:
            print("Thanks for using our system.")
            break


if __name__ == "__main__":
    main()