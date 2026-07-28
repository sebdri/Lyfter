def menu():

    while True:

        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Show Available Books")
        print("5. Export to CSV")
        print("6. Import from CSV")
        print("7. Exit")

        try:

            option = int(input("Please enter the desired option: "))

            if 1 <= option <= 7:
                return option

            else:
                print("Please choose a number between 1 and 7.")

        except ValueError:
            print("Invalid data.")