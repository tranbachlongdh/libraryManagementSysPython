import sys

from encrypt_string import *
from library import Library
from user import Admin, UserManager

hiddenAdmin = Admin('Long', 'Tran', 'admin', 'admin@admin.com', 'admin123456')


def displayMenu():
    print("""== == == LIBRARY MENU == == ==
        1. Display all available books
        2. Request a book
        3. Return a book
        4. Special function
        5. User profile
        6. Logout
        7. Exit
        """)
    return int(input("Enter Choice:"))


def special_func(user):
    if user.prior == 0:
        print("""Normal user:
                1. Back
                """)
        return int(input("Enter Choice:"))
    elif user.prior == 1:
        print("""Moderator:
                1. Add new book
                2. List all users
                3. Add user
                4. Back
                """)
        return int(input("Enter Choice:"))
    elif user.prior == 2:
        print("""Admin:
                1. Add new book
                2. Remove book
                3. List all users
                4. Add user
                5. Remove user
                6. Upgrage user
                7. Back
                """)
        return int(input("Enter Choice:"))

def pass_change(user):
    password = input('New password: ')
    retypepass = input('Re-type new password: ')
    if (len(password) > 6) and (password == retypepass):
        user.edit_password(password)
        print('Password has been changed.')
    else:
        print('New password is invalid.')


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
                  2. Sign in
                  3. About
                  4. Exit
                  """)
            choice = int(input("Enter Choice:"))
            if choice == 0:
                username = input("Username: ")
                password = input("Password: ")
                if (username == hiddenAdmin.username) and (password == decode_string(hiddenAdmin.password)):
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
                choice = special_func(current_user)
                if current_user.prior == 0:
                    if choice == 1:
                        back = True
                elif current_user.prior == 1:
                    if choice == 1:
                        library.add_book_manual(current_user)
                    elif choice == 2:
                        userManager.list_all_user()
                    elif choice == 3:
                        userManager.add_newUser()
                    elif choice == 3:
                        back = True
                elif current_user.prior == 2:
                    if choice == 1:
                        library.add_book_manual(current_user)
                    elif choice == 2:
                        pass
                    elif choice == 3:
                        userManager.list_all_user()
                    elif choice == 4:
                        userManager.add_newUser()
                    elif choice == 5:
                        pass
                    elif choice == 6:
                        pass
                    elif choice == 7:
                        back = True
        elif choice == 5:
            current_user.show_userInfo()

            back = False
            while not back:
                print("""User profile
                1. Edit profile
                2. Change password
                3. Back
                """)
                choice = int(input("Enter Choice:"))
                if choice == 1:
                    pass
                elif choice == 2:
                    pass_change(current_user)
                elif choice == 3:
                    back = True
        elif choice == 6:
            current_user = None
            userManager.isLogin = False
            print('Logged out!!!')
        elif choice == 7:
            sys.exit()
        else:
            print("Please choose options in the list!!!\n")


if __name__ == "__main__":
    main()
    #library = Library()
    #userManager = UserManager()
    
    
    #library.add_book_manual(current_user)
