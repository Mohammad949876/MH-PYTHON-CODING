print("GreenWood library")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "available"

class Library:
    def __init__(self):
        self.book = []

    def add_book(self):
        book_id = input("Enter Book ID: ")

        for book in self.book:
            if book.book_id == book_id:
                print("A book with this ID Already Exists.")
                return
        title = input("Enter Book title: ")
        author = input("Enter author's name: ")

        new_book = Book(book_id, title, author)
        self.book.list(new_book)

        print("Book Added successfully")

    def borrow_book(self):
        book_id = input("Enter book ID: ")

        for book in self.book:
            if book.book_id == book.id:
                if book.status == "available":
                    book.status = "Borrowed"
                    print("Book borrowed Successfully")
                else:
                    print("the book has already been borrowed")
                return

        print("Book id not found")

    def return_book(self):
        book_id = input("Enter book id:")

        for book in self.book:
            if book.book_id == book_id:
                if book.status == "borrowed":
                    book.status = "available"
                    print("Book returned successfully")
                else:
                    print("Book has not been borrowed yet")
                return

        print("Book id not found")

    def books_available(self):
        print("\n===== Available books =====")

        found = False

        for book in self.book:
            if book.status == "Available":
                print("Book id:" book.book_id)
                print("title:" book.title)
                print("author:" book.author)
                print("status:" book.status)
                print("=====================")
                found = True

        if not found:
            print("Book is not available in the library right now.")

    def All_the_books(self):
        print("\n===== All the books")

        if len(self.book) == 0:
            print("There are not book right now.")
            return

        for book in self.book:
            if book.status == "Available":
                print("Book id:" book.book_id)
                print("title:" book.title)
                print("author:" book.author)
                print("status:" book.status)
                print("=====================")

    def main():
        library = Library()

        while True:
            print("\n ===== Greenwood Community library")
            print("1. add a book")
            print("2. borrow a book")
            print("3. return a book")
            print("4. view available book")
            print("5. View all the books")
            print("6. Exit")

            

