library = {}

while True:
    print("\n===== Library Management =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        library[book_id] = {"Title": title, "Author": author}
        print("Book Added Successfully!")

    elif choice == "2":
        if library:
            print("\nAvailable Books:")
            for bid, details in library.items():
                print(f"Book ID : {bid}")
                print(f"Title   : {details['Title']}")
                print(f"Author  : {details['Author']}")
                print("-" * 25)
        else:
            print("No books available.")

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        if book_id in library:
            print(library[book_id])
        else:
            print("Book Not Found!")

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        if book_id in library:
            del library[book_id]
            print("Book Removed Successfully!")
        else:
            print("Book Not Found!")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")