import csv


def export_data(file_path, books):

    if len(books) == 0:
        print("There is no data to export.")
        return

    with open(file_path, "w", encoding="utf-8", newline="") as file:

        headers = books[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writeheader()

        writer.writerows(books)

    print("Books exported successfully.")


def import_data(file_path, books):

    try:

        with open(file_path, "r", encoding="utf-8", newline="") as file:

            reader = csv.DictReader(file)

            books.clear()

            for book in reader:

                book["Year"] = int(book["Year"])

                books.append(book)

        print("Books imported successfully.")

        return books

    except FileNotFoundError:

        print("No data has been previously exported.")

        return books