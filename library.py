from book import Book
#from user import *


class Library:
    maxBooksBorrow = 3

    def __init__(self):
        self.availablebooks = []

    def add_book_manual(self, user):
        if user.prior >= 1:
            print("Please enter the book's information:")
            isbn = input("isbn: ")
            title = input("Book title: ")
            subject = input("Subject: ")
            author = input("Author: ")
            publisher = input("Publisher: ")
            date = input("Publish date: ")
            pages = int(input("Pages: "))
            copies = int(input("Copies: "))

            self.availablebooks.append(Book(isbn, title, subject, author, publisher, date, pages, copies))
        else:
            print("You don't have the right to add new book.")


    def displayAvailablebooks(self):
        print("================================================")
        print("We have {} books are available in our library:".format(Book.count))
        print("------------------------------------------------")
        for bk in self.availablebooks:
            print("{}. {}".format(self.availablebooks.index(bk)+1, bk))

    #This func is for checking the availability of book in system
    #Input: isbn
    #Output:
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

    def getBookReturn(self, user, returnedBook):
        if returnedBook != None:
            for bk in self.availablebooks:
                if bk.isbn == str(returnedBook):
                    bk.copies += 1
                    print("Thanks for returning your borrowed book")
                    print("You are still keeping {} books: {}".format(user.noBooksBorrowed, user.showBooksBorrowed()))
                    return 1
        else:
            print('isbn number you have entered is incorrect.')
            return 0


        # return 1
