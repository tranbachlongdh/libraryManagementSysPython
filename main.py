from library import Library
from user import User, Admin, UserManager
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

hiddenAdmin = Admin('Long', 'Tran', 'admin', 'admin@admin.com', 'admin123456')

def displayMenu():
    print("""== == == LIBRARY MENU == == ==
        1. Display all available books
        2. Request a book
        3. Return a book
        4. User profile
        5. Logout
        6. Exit
        """)
    return int(input("Enter Choice:"))

def norDisplayMenu():
    print("""Normal user:
        1. Change your profile
        2. Change your password
        3. Back
        """)
    return int(input("Enter Choice:"))

def moderatorDisplayMenu():
    print("""Moderator:
        1. Change your profile
        2. Change your password
        3. Add new book
        4. Add/remove user
        5. Back
        """)
    return int(input("Enter Choice:"))

def adminDisplayMenu():
    print("""Admin:
        1. Your profile
        2. Change your profile
        3. Add/remove new book
        4. Add/remove user
        5. Upgrage user
        6. Back
        """)
    return int(input("Enter Choice:"))

def main():
    library = Library()
    userManager = UserManager()
    #norUser = Admin("Long", 'Tran', 'rose4u', 'tranbachlongdh@gmail.com', 'youaremyHero#1', 20)
    # admin1 = Admin("12345", "tol1hc", "12345")
    current_user = None
    #userTemp = norUser
    
    while True:
        while not userManager.isLogin:
            print("""== == == Welcome to library management sys.== == == 
                  1. Login
                  2. Signin
                  3. About
                  4. Exit
                  """)
            choice = int(input("Enter Choice:"))
            if choice == 0:
                username = input("Username: ")
                password = input("Password: ")
                if (username == hiddenAdmin.username) and (password == hiddenAdmin.password):
                    current_user = hiddenAdmin
                    userManager.isLogin = True
                    print("You've logged in as Hidden Admin")
                    
            elif choice == 1:
                current_user = userManager.login()
            elif choice == 2:
                userManager.add_newUser()
            elif choice == 3:
                print("""== == == LIBRARY MANAGEMENT SYSTEM== == == 
                  Author: Tran Bach Long
                  Created: 2019
                  """)
            elif choice == 4:
                sys.exit()
            else:
                print("Please choose options in the list!!!\n")

        choice = displayMenu()
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lendBook(current_user, current_user.requestBook)
        elif choice == 3:
            library.getBookReturn(current_user, current_user.returnBook)
        elif choice == 4:
            back = False
            while not back:
                current_user.show_userInfo()
                if current_user.prior == 0:
                    choice = norDisplayMenu()
                    if choice == 1:
                        pass
                    elif choice == 2:
                        pass
                    elif choice == 3:
                        back = True
                elif current_user.prior == 1:
                    choice = moderatorDisplayMenu()
                    if choice == 1:
                        pass
                    elif choice == 2:
                        pass
                    elif choice == 3:
                        pass
                    elif choice == 4:
                        pass
                    elif choice == 5:
                        back = True
                elif current_user.prior == 2:
                    choice = adminDisplayMenu()
                    if choice == 1:
                        pass
                    elif choice == 2:
                        pass
                    elif choice == 3:
                        pass
                    elif choice == 4:
                        pass
                    elif choice == 5:
                        pass
                    elif choice == 6:
                        back = True
            
        elif choice == 5:
            current_user = None
            userManager.isLogin = False
        elif choice == 6:
            sys.exit()
        else:
            print("Please choose options in the list!!!\n")


if __name__ == "__main__":
    main()
    #library = Library()
    #userManager = UserManager()
    
    
    #library.add_book_manual(current_user)
