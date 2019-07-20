import json
import os
import sys

from encrypt_string import *
from library import Library
from user import Admin, UserManager

hiddenAdmin = Admin('Long', 'Tran', 'admin', 'admin@admin.com', 'admin123456', userid="user000")


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
    return input("Enter Choice>>")


def special_func_menu(user):
    if user.prior == 0:
        print("""Normal user:
        1. Back
        """)
        return input("Enter Choice>>")
    elif user.prior == 1:
        print("""Moderator:
        1. Add new book
        2. List all users
        3. Add user
        4. Back
        """)
        return input("Enter Choice>>")
    elif user.prior == 2:
        print("""Admin:
        1. Add new book
        2. Remove book
        3. List all users
        4. Add user
        5. Remove user
        6. Upgrage user
        7. Downgrage user
        8. Back
        9. Export users list
        """)
        return input("Enter Choice>>")


def add_book_menu():
    print("""Add new book:
        1. Manually
        2. Import from file
        3. Back
        """)
    return input("Enter Choice>>")


def pass_change(user):
    password = input('New password: ')
    retypepass = input('Re-type new password: ')
    if (len(password) > 6) and (password == retypepass):
        user.edit_password(password)
        print('Password has been changed.')
    else:
        print('New password is invalid.')


def post_run(users, books, path):
    output = users.user_data_2json()
    output.update(books.book_data_2json())
    with open(path, 'w') as outfile:
        json.dump(output, outfile)


def main():
    databasepath = 'sources/database.json'
    if not os.path.isfile(databasepath):
        print(databasepath + " is not found.")
        anw = input("Do you want to create new one? (Y/N)>>")
        if anw == 'Y' or anw == 'y':
            data = {"user_data":[], "book_data":[]}
            with open(databasepath, 'w') as outfile:
                json.dump(data, outfile)
        else:
            sys.exit()
    library = Library()
    library.add_book_fromFile(databasepath)
    userManager = UserManager()
    current_user = None
    userManager.add_userFromFile(databasepath)
    
    while True:
        while not userManager.isLogin:
            print("""== == == Welcome to library management sys.== == == 
              1. Login
              2. Sign in
              3. About
              4. Exit
              """)
            choice = input("Enter Choice>>")
            if choice == '0':
                username = input("Username: ")
                password = input("Password: ")
                if (username == hiddenAdmin.username) and (password == decode_string(hiddenAdmin.password)):
                    current_user = hiddenAdmin
                    userManager.isLogin = True
                    print("You've logged in as Hidden Admin")
                    
            elif choice == '1':
                current_user = userManager.login()
            elif choice == '2':
                userManager.add_newUser()
            elif choice == '3':
                print("""== == == LIBRARY MANAGEMENT SYSTEM== == == 
                  Author: Tran Bach Long
                  Created: 2019
                  """)
            elif choice == '4':
                sys.exit()
            else:
                print("Please choose options in the list!!!\n")

        choice = displayMenu()
        if choice == '1':
            library.displayAvailablebooks()
        elif choice == '2':
            library.lendBook(current_user, current_user.requestBook())
        elif choice == '3':
            library.getBookReturn(current_user, current_user.returnBook())
        elif choice == '4':
            back = False
            while not back:
                choice = special_func_menu(current_user)
                if current_user.prior == 0:
                    if choice == '1':
                        back = True
                elif current_user.prior == 1:
                    if choice == '1':
                        add_choice = add_book_menu()
                        if add_choice == '1':
                            library.add_book_manual()
                        elif add_choice == '2':
                            path = input("Enter path to data file>>")
                            library.add_book_fromFile(path)
                        elif add_choice == '3':
                            back = True
                        else:
                            print("Please choose in the list!!!")

                    elif choice == '2':
                        userManager.list_all_user()
                    elif choice == '3':
                        userManager.add_newUser()
                    elif choice == '4':
                        back = True
                elif current_user.prior == 2:
                    if choice == '1':
                        sub_choice = add_book_menu()
                        if sub_choice == '1':
                            library.add_book_manual()
                        elif sub_choice == '2':
                            path = input("Enter path to data file>>")
                            library.add_book_fromFile(path)
                        elif sub_choice == '3':
                            back = True
                        else:
                            print("Please choose in the list!!!")
                    elif choice == '2':
                        pass
                    elif choice == '3':
                        userManager.list_all_user()
                    elif choice == '4':
                        userManager.add_newUser()
                    elif choice == '5':
                        pass
                    elif choice == '6':
                        dest_userid = input("Enter which user to be upgraded>>")
                        userManager.upgrade_downgrade_user(dest_userid, "up")
                    elif choice == '7':
                        dest_userid = input("Enter which user to be downgraded>>")
                        userManager.upgrade_downgrade_user(dest_userid, "down")
                    elif choice == '8':
                        back = True
                    elif choice == '9':
                        user_list_json = userManager.user_data_2json()
                        with open('sources/user_list.json', 'w') as outfile:
                            json.dump(user_list_json, outfile)
                    else:
                        print("Please choose options in the list!!!\n")
        elif choice == '5':
            current_user.show_userInfo()

            back = False
            while not back:
                print("""User profile
                1. Edit profile
                2. Change password
                3. Books borrowed list
                4. Back
                """)
                sub_choice = input("Enter Choice>>")
                if sub_choice == '1':
                    pass
                elif sub_choice == '2':
                    pass_change(current_user)
                elif sub_choice == '3':
                    print(current_user.showBooksBorrowed())
                elif sub_choice == '4':
                    back = True
                else:
                    print("Please choose options in the list!!!\n")
        elif choice == '6':
            userManager.logout(current_user)
            post_run(userManager, library, 'sources/database.json')
        elif choice == '7':
            post_run(userManager, library, 'sources/database.json')
            print("System exit!!!")
            sys.exit()
        else:
            print("Please choose options in the list!!!\n")


if __name__ == "__main__":
    main()
