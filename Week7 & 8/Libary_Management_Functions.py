global books
books = []

class Book:
    def __init__(self, title, author, copies, borrowed, due_date):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = borrowed
        self.due_date = due_date 

    def addBooks(title, author, copies):
        print("This is for adding of books")
        newBooks = {"title": title, "author": author, "copies": copies }
        books.append(newBooks)
        return newBooks

    def viewBooks():
        return books

    def borrowBooks():
       
        


class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []
        self.users = []
