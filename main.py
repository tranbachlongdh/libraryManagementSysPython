from library import Library
from user import *
import sys


# book_1 = Book("0-7475-3269-8", "Avengers", "Comics", "Stan Lee", "Marvel Comics", "2/5/1963", 58, 1)
# book_2 = Book("0-7475-3269-9", "Harry Potter", "Novel", "J.K. Rowling", "Bloomsbury", "26/6/1997", 223, 5)
# library = Library()
# library.add_book_manual()
# library.displayAvailablebooks()
#
# norUser = User("25g23", "put1hc", "123432")
# admin1 = Admin("12345", "tol1hc", "12345")
#
#
# print(norUser)
# print(admin1)
#
# print(norUser.noBookBorrowed)
# library.lendBook(norUser, norUser.requestBook)
# library.lendBook(norUser, norUser.requestBook)
#
# library.displayAvailablebooks()
#
# library.getBookReturn(norUser, norUser.returnBook)
def main():
    library = Library()
    norUser = Admin("Long", 'Tran', 'rose4u', 'tranbachlongdh@gmail.com', 'youaremyHero#1', 20)
    # admin1 = Admin("12345", "tol1hc", "12345")
    userTemp = norUser
    print("Welcome to library management sys.")
    while True:
        print("""== == == LIBRARY MENU == == ==
                1. Display all available books
                2. Add new book
                3. Request a book
                4. Return a book
                5. Exit
                6. Add new user
                """)

        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.add_book_manual(userTemp)
        elif choice == 3:
            library.lendBook(userTemp, userTemp.requestBook)
        elif choice == 4:
            library.getBookReturn(userTemp, userTemp.returnBook)
        elif choice == 5:
            sys.exit()
        elif choice == 6:
            print(library.userlist)
            library.add_newUser()
        else:
            print("Please choose options in the list!!!\n")


if __name__ == "__main__":
    main()
