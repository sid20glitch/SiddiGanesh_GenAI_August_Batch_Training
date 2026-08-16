def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog:
        if book_id not in borrowed_books:
            borrowed_books.append(book_id)
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed.")
    else:
        print("Book does not exist.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print("Book returned successfully.")
    else:
        print("Book was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id in catalog:
        if book_id not in borrowed_books:
            title, author, year = catalog[book_id]
            print(f"ID: {book_id}")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Year: {year}")
            print()


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Adding books
    add_book(catalog, 101, "Python Basics", "Guido", 2020)
    add_book(catalog, 102, "Java Programming", "James Gosling", 2019)
    add_book(catalog, 103, "Data Structures", "Mark Allen", 2021)
    add_book(catalog, 104, "Algorithms", "Robert Sedgewick", 2018)

    # Registering members
    register_member(members, 1)
    register_member(members, 2)
    register_member(members, 3)
    register_member(members, 2)      

    # Borrow books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    # Return one book
    return_book(borrowed_books, 101)

    # Show available books
    show_available(catalog, borrowed_books)

    print("Members:", members)
    print("Borrowed Books:", borrowed_books)


main()