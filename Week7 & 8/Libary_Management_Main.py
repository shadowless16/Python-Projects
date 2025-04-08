import Libary_Management_Functions



"""Welcome Msg"""
print("Welcome to the Libary mangemnt system app.")

while True:

    choice = int(input("Whcih of the option wouldyou like to pick ? \n1.Add Books \n2. View Books"))

    # book1 = Book("ak book", "me", 6, 3, 12/32/2025)
    if choice == 1:
        title = input("enter book title: ")
        author = input("Enter book authour: ")
        copies = input("Enter the book Copies: ")

        newBooks = Libary_Management_Functions.Book.addBooks(title, author, copies)
        print(newBooks)
    elif choice == 2:
        books = Libary_Management_Functions.Book.viewBooks()

        if books:
            for i,book in enumerate(books, start=1):
                print(f"{i} Name: {book['title']}, Author: {book['author']}, Copies: {book['copies']}")
        else:
            print("No tasks to show.")

