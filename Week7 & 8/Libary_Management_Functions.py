from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {} 
        self.users = {} 
        self.fine_per_day = 1000

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists!")
            return
        self.books[book_id] = Book(book_id, title, author)
        print(f"Added book: {title} by {author}")

    def remove_book(self, book_id):
        if book_id not in self.books:
            print(f"Book ID {book_id} not found!")
            return
        if self.books[book_id].is_borrowed:
            print(f"Cannot remove book {book_id}, it is currently borrowed!")
            return
        del self.books[book_id]
        print(f"Removed book ID {book_id}")

    def add_user(self, user_id, name):
        if user_id in self.users:
            print(f"User ID {user_id} already exists!")
            return
        self.users[user_id] = User(user_id, name)
        print(f"Added user: {name}")

    def remove_user(self, user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} not found!")
            return
        if self.users[user_id].borrowed_books:
            print(f"Cannot remove user {user_id}, they have borrowed books!")
            return
        del self.users[user_id]
        print(f"Removed user ID {user_id}")

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            print(f"User ID {user_id} not found!")
            return
        if book_id not in self.books:
            print(f"Book ID {book_id} not found!")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if book.is_borrowed:
            print(f"Book {book.title} is already borrowed!")
            return

        book.is_borrowed = True
        book.borrowed_by = user_id
        book.due_date = datetime.now() + timedelta(days=14)  # 2-week borrowing period
        user.borrowed_books.append(book_id)
        print(f"{user.name} borrowed {book.title}. Due date: {book.due_date}")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print(f"User ID {user_id} not found!")
            return
        if book_id not in self.books:
            print(f"Book ID {book_id} not found!")
            return

        book = self.books[book_id]
        user = self.users[user_id]

        if not book.is_borrowed or book.borrowed_by != user_id:
            print(f"Book {book.title} is not borrowed by {user.name}!")
            return

        fine = self.calculate_fine(book)
        book.is_borrowed = False
        book.borrowed_by = None
        book.due_date = None
        user.borrowed_books.remove(book_id)
        print(f"{user.name} returned {book.title}.")
        if fine > 0:
            print(f"Fine for overdue book: ₦{fine:.2f}")

    def calculate_fine(self, book):
        if not book.due_date:
            return 0.0
        days_overdue = (datetime.now() - book.due_date).days
        if days_overdue > 0:
            return days_overdue * self.fine_per_day
        return 0.0

    def view_borrowed_books(self, user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} not found!")
            return
        user = self.users[user_id]
        if not user.borrowed_books:
            print(f"{user.name} has no borrowed books.")
            return
        print(f"{user.name}'s borrowed books:")
        for book_id in user.borrowed_books:
            book = self.books[book_id]
            fine = self.calculate_fine(book)
            print(f"- {book.title} (Due: {book.due_date}) Fine: ₦{fine:.2f}")

    def list_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book_id, book in self.books.items():
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Status: {status}")

    def list_all_users(self):
        if not self.users:
            print("No users in the library.")
            return
        print("Users in the library:")
        for user_id, user in self.users.items():
            print(f"ID: {user_id}, Name: {user.name}")

def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add User")
        print("4. Remove User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View Borrowed Books")
        print("8. List All Books")
        print("9. List All Users")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.add_book(book_id, title, author)

        elif choice == "2":
            book_id = int(input("Enter Book ID to remove: "))
            library.remove_book(book_id)

        elif choice == "3":
            user_id = int(input("Enter User ID: "))
            name = input("Enter User Name: ")
            library.add_user(user_id, name)

        elif choice == "4":
            user_id = int(input("Enter User ID to remove: "))
            library.remove_user(user_id)

        elif choice == "5":
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            library.borrow_book(user_id, book_id)

        elif choice == "6":
            user_id = int(input("Enter User ID: "))
            book_id = int(input("Enter Book ID: "))
            library.return_book(user_id, book_id)

        elif choice == "7":
            user_id = int(input("Enter User ID: "))
            library.view_borrowed_books(user_id)

        elif choice == "8":
            library.list_all_books()

        elif choice == "9":
            library.list_all_users()

        elif choice == "10":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()