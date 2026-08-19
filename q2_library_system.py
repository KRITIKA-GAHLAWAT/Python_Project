
def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Book {book_id} cannot be borrowed.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")

    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"{book_id}: {title} by {author} ({year})")


def main():

    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 101, "Python Basics", "John Smith", 2022)
    add_book(catalog, 102, "Learning Python", "Mark Lee", 2021)
    add_book(catalog, 103, "Python Advanced", "Sarah Khan", 2023)
    add_book(catalog, 104, "Data Science", "David Brown", 2020)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")

    register_member(members, "M001")

    print("Members:", members)

    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 102)

    print("Borrowed books:", borrowed_books)

    return_book(borrowed_books, 101)

    print("Borrowed books after return:", borrowed_books)

    show_available(catalog, borrowed_books)


main()
