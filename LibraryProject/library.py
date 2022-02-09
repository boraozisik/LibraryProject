import sqlite3

import time

class Book():

    def __init__(self, name, author, publisher, type, edition):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.type = type
        self.edition = edition

    def __str__(self):
        return "Name of the book: {}\nAuthor of the book: {}\nPublisher of the book: {}\nType of the book: {}\nEdition of the book: {}\n" .format(self.name, self.author, self.publisher, self.type, self.edition)


class Library():

    def __init__(self):
        self.create_link()

    def create_link(self):
        self.connection = sqlite3.connect("library.db")

        self.cursor = self.connection.cursor()

        query = "Create Table If not exists books (name TEXT,author TEXT,publisher TEXT,type TEXT,edition INT)"

        self.cursor.execute(query)

        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def show_books(self):
        query = "Select * From books"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if(len(books) == 0):
            print("There is not any book in this library.")

        else:
            for i in books:
                book = Book(i[0], i[1], i[2], i[3], i[4])
                print(book)


    def search_book(self,name):
        query = "Select * From books where name = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is not a book with this name.")

        else:
            book = Book(books[0][0], books[0][1], books[0][2], books[0][3], books[0][4])

            print(book)

    def add_book(self,book):

        query = "Insert into books Values(?,?,?,?,?)"

        self.cursor.execute(query, (book.name,book.author,book.publisher,book.type,book.edition))

        self.connection.commit()


    def remove_book(self,name):

        query = "Delete From books where name = ?"

        self.cursor.execute(query, (name,))

        self.connection.commit()


    def upgrade_edition(self,name):

        query = "Select * From books where name = ?"

        self.cursor.execute(query, (name,))

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("There is not a book with this name.")

        else:
            edition = books[0][4]

            edition += 1

            query2 = "Update books set edition = ? where name = ?"

            self.cursor.execute(query2, (edition,name))

            self.connection.commit()

