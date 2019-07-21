import json
import os

from book import Book


class Library:
    maxBooksBorrow = 3

    def __init__(self):
        self.availablebooks = []

    # This func is for adding 1 new book's data to library management system manually
    # Output:
    #   new book will be added to book list
    def add_book_manual(self):
        print("Please enter the book's information:")
        flag = [False]*2
        cancel = "N"
        while not (flag[0] & flag[1]) and not (cancel == "Y" or cancel == 'y'):
            isbn = input("isbn: ").strip()
            title = input("Book title: ").strip()

            for tmpbook in self.availablebooks:
                if tmpbook.isbn == isbn:
                    return

            if isbn == '':
                print("isbn should be filled.")
                flag[0] = False
            else:
                flag[0] = True

            if title == '':
                print("title should be filled.")
                flag[1] = False
            else:
                flag[1] = True

            if not (flag[0] & flag[1]):
                cancel = input("Cancel? (Y/N)>>")
        if cancel == "Y" or cancel == 'y':
            return print("Add book canceled!")
        subject = input("Subject: ").strip()
        author = input("Author: ").strip()
        publisher = input("Publisher: ").strip()
        date = input("Publish date: ").strip()
        pages = input("Pages: ").strip()
        copies = input("No. of copies: ").strip()
        copies = 1 if copies == '' else int(copies)

        self.availablebooks.append(Book(isbn, title, subject, author, publisher, date, pages, copies))

    def add_book_fromFile(self, path):
        if os.path.isfile(path):
            datafile = json.load(open(path, 'r'))
            for i in range(len(datafile["book_data"])):
                isbn = datafile["book_data"][i]["isbn"]
                for tmpbook in self.availablebooks:
                    if tmpbook.isbn == isbn:
                        return
                title = datafile["book_data"][i]["title"]
                subject = datafile["book_data"][i]["subject"]
                author = datafile["book_data"][i]["author"]
                publisher = datafile["book_data"][i]["publisher"]
                date = datafile["book_data"][i]["date"]
                pages = int(datafile["book_data"][i]["pages"])
                copies = int(datafile["book_data"][i]["copies"])

                self.availablebooks.append(Book(isbn, title, subject, author, publisher, date, pages, copies))
            print("Books have been added to library.")
        else:
            print(path + " is not found.")

    def export_book_toFile(self, path):
        pass

    # Display available books to screen
    def displayAvailablebooks(self):
        print("================================================")
        print("We have {} books are available in our library:".format(Book.count))
        print("------------------------------------------------")
        for bk in self.availablebooks:
            print("{}. {}".format(self.availablebooks.index(bk)+1, bk))

    # This func is for checking the availability of book in system
    # Input: isbn
    # Output:
    #   Not available in system: return -2
    #   Borrow by someone else: return -1
    def checkAvailability(self, isbn):
        for bk in self.availablebooks:
            if isbn == bk.isbn:
                if bk.copies > 0:
                    return self.availablebooks.index(bk)
                else:
                    return -1
        return -2

    # Lend 1 book to a user by isbn
    # Input: user
    # Input: isbn
    # Output:
    #   remove lent book from library
    #   add book info to user profile
    def lendBook(self, user, requestedBook):
        if user.noBooksBorrowed >= Library.maxBooksBorrow:
            print("You have reached limit. You can only borrow 3 books, please return lent books before borrowing")
        else:
            available = self.checkAvailability(str(requestedBook))
            if available == -2:
                print('The book you requested is not available.')
            elif available == -1:
                print('Sorry the book you have requested is currently not in the library')
            else:
                for bk in user.booksBorrowed:
                    if str(requestedBook) == bk:
                        asw = input('You have already borrowed the same book. '
                                    'Do you want to borrow the same one? (Y/N)>>')
                        if asw == 'Y' or asw == 'y':
                            print("The book you requested has now been borrowed")
                            self.availablebooks[available].copies -= 1
                            user.noBooksBorrowed += 1
                            user.edit_booksBorrowed(str(requestedBook))
                            return 1
                        else:
                            print("Cancel!")
                            return 0
                print("The book you requested has now been borrowed")
                self.availablebooks[available].copies -= 1
                user.noBooksBorrowed += 1
                user.edit_booksBorrowed(str(requestedBook))

    # Receive book return from user who borrowed it
    # Input: user
    # Input: isbn
    # Output:
    #   add return book to library
    #   remove book info from user profile
    def getBookReturn(self, user, returnedBook):
        if returnedBook is not None:
            for bk in self.availablebooks:
                if bk.isbn == str(returnedBook):
                    bk.copies += 1
                    print("Thanks for returning your borrowed book")
                    print("You are still keeping {} books: {}".format(user.noBooksBorrowed, user.showBooksBorrowed()))
                    return 1
        else:
            print('isbn number you have entered is incorrect.')
            return 0

    # Convert book data list to json string
    # Input: availablebooks
    # Output: data in json format
    def book_data_2json(self):
        data = {}
        data["book_data"] = []
        for each_book in self.availablebooks:
            data['book_data'].append({
                "isbn": each_book.isbn,
                "title": each_book.title,
                "subject": each_book.subject,
                "author": each_book.author,
                "publisher": each_book.publisher,
                "date": each_book.date,
                "pages": each_book.pages,
                "copies": each_book.copies
            })
        return data