from library import *

print(""""*********************************
---WELCOME TO LIBRARY---

Options:
1- Show Books
2- Search Book
3- Add book
4- Remove book
5- Upgrade edition

For exit, press "q".

*********************************""")

library = Library()

while True:

    option = input("Enter your option number:")

    if(option == "q"):
        print("Exiting from library...")
        break
    elif(option == "1"):
        library.show_books()
    elif (option == "2"):
        name = input("Enter the name of your book that you want to search:")
        print("Searching for your book...")
        time.sleep(3)
        library.search_book(name)
    elif (option == "3"):
        name = input("Enter the name of your book:")
        author = input("Enter the author of your book:")
        publisher = input("Enter the publisher of your book:")
        type = input("Enter the type of your book:")
        edition = int(input("Enter the edition of your book:"))
        new_book = Book(name,author,publisher,type,edition)
        print("Your book is adding to library...")
        time.sleep(3)
        library.add_book(new_book)
        print("Your book has been added.")

    elif (option == "4"):
        name = input("Enter the name of your book that you want to remove:")
        answer = input("Your book will be deleted, are you sure? (yes / no)")
        if(answer == "yes"):
            print("Your book is removing...")
            time.sleep(3)
            library.remove_book(name)
            print("Your book has been removed.")

    elif (option == "5"):
        name = input("Enter the name of your book that you want to upgrade its edition:")
        print("Edition is upgrading...")
        time.sleep(5)
        library.upgrade_edition(name)
        print("Edition upgraded.")
    else:
        print("Invalid option number!!")
























