# Simple Library Book Manager !!

library = []  # This list will store all the books.

# Add a new book.
def add_book():
    name = input("Enter the book name: ")
    writer = input("Enter the author's name: ")
    library.append([name, writer])
    print("Book added successfully!\n")

# Search for a book by name
def search_book():
    search_name = input("Enter the book name to search: ")
    for book in library:
        if book[0].lower() == search_name.lower():
            print(f"Found: '{book[0]}' by {book[1]}\n")
            return
    print("Book not found.\n")

# Show all books in the library.
def show_books():
    if not library:
        print("No books in the library yet.\n")
    else:
        print("List of all books:")
        for book in library:
            print(f"- {book[0]} by {book[1]}")
        print()

# Main menu loop.
while True:
    print("Library Menu:")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Show All Books")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        show_books()
    elif choice == "4":
        print("Exiting the Library Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")