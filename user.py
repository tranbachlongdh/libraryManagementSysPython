import json

from encrypt_string import *


class User:
    prior = 0
    count = 0

    def __init__(self, firstname, lastname, username, email, password, age=None, userid=None):
        User.count += 1
        self.firstname = firstname
        self.lastname = lastname
        self.userid = userid
        if self.userid != None:
            self.userid = userid
        else:
            self.userid = "user" + ('00' if User.count < 10 else '0' if User.count < 100 else '') + str(User.count)
        self.username = username
        self.email = email
        self.password = encode_string(password)
        self.age = age
        self.bookBorrowed = []
        self.noBookBorrowed = 0

    def edit_firstname(self, updated_firstname):
        self.firstname = updated_firstname

    def edit_lastname(self, updated_lastname):
        self.lastname = updated_lastname

    def edit_age(self, updated_age):
        self.age = updated_age

    def edit_password(self, update_password):
        self.password = encode_string(update_password)

    def show_userInfo(self):
        print("-------------------------------------------------------------")
        print("UserID: " + str(self.userid))
        print("Username: " + str(self.username))
        print("Email: " + str(self.email))
        print("Full name: {} {}".format(str(self.firstname), str(self.lastname)))
        print("Age: Unknown") if self.age == None else print("Age: {} years old".format(str(self.age)))
        print("Right: Admin.") if self.prior == 2 \
            else (print("Right: Moderator.") if self.prior == 1 else print("Right: Normal user."))
        print("-------------------------------------------------------------")
        return 1

    @property
    def requestBook(self):
        print("Enter the isbn of the book you'd like to borrow>>")
        self.bookisbn = input()
        return self.bookisbn

    @property
    def showBookBorrowed(self):
        return self.bookBorrowed

    def edit_bookBorrowed(self, isbn):
        self.bookBorrowed.append(isbn)

    @property
    def returnBook(self):
        print("Enter the isbn of the book you'd like to return>>")
        self.bookisbn = input()
        if self.bookisbn in(self.bookBorrowed):
            self.noBookBorrowed -= 1
            self.bookBorrowed.remove(self.bookisbn)
            return self.bookisbn
        return None

    def __repr__(self):
        return type(self).__name__ + '({}, {})'.format(self.userid, self.username)

    def __str__(self):
        return '{} - {} - {} {} - {} - {} - ({})'\
                        .format(self.userid, \
                                self.username, \
                                self.firstname, self.lastname, \
                                self.email,\
                                self.age, \
                                type(self).__name__)
    
    @property
    def userUp2Mod(self):
        self.__class__ = Moderator
        print("User {} has been upgrage to Moderator.".format(self.userid))
        
    @property
    def userDown2Nor(self):
        if self.prior == 0:
            print("This user is Normal user already.")
        else:
            self.__class__ = User
            print("User {} has been downgrage to Normal user.".format(self.userid))
        

class Admin(User):
    prior = 2

    def __init__(self, firstname, lastname, username, email, password, age=None, userid=None):
        super().__init__(firstname, lastname, username, email, password, age, userid)
        

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


class Moderator(User):
    prior = 1

    def __init__(self, firstname, lastname, username, email, password, age=None, userid=None):
        super().__init__(firstname, lastname, username, email, password, age, userid)
        
    @property
    def userUp2Admin(self):
        self.__class__ = Admin
        print("User {} has been upgrage to Admin.".format(self.userid))

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


class UserManager:
    def __init__(self):
        self.userlist = []
        self.isLogin = False
        
    def login(self):
        loginname = input("Username/Email: ")
        password = input("Password: ")
        for each in self.userlist:
            if ((each.username == loginname) or (each.email == loginname)) \
                    and (decode_string(each.password) == password):
                self.isLogin = True
                return each
        print("Login fail. Username or password is incorrect.")
        return None

    def add_userFromFile(self, path):
        datafile = json.load(open(path, 'r'))
        # print(datafile["user_data"][1]["userid"])
        for i in range(len(datafile["user_data"])):
            firstname = datafile["user_data"][i]["firstname"]
            lastname = datafile["user_data"][i]["lastname"]
            username = datafile["user_data"][i]["username"]
            userid = datafile["user_data"][i]["userid"]
            email = datafile["user_data"][i]["email"]
            password = bytes(datafile["user_data"][i]["password"], 'utf-8')
            age = datafile["user_data"][i]["age"]
            prior = datafile["user_data"][i]["prior"]
            if prior == 0:
                self.userlist.append(User(firstname, lastname, username, email, decode_string(password), age, userid))
            elif prior == 1:
                self.userlist.append(Moderator(firstname, lastname, username, email, decode_string(password), age, userid))
            elif prior == 2:
                self.userlist.append(Admin(firstname, lastname, username, email, decode_string(password), age, userid))
    
    def add_newUser(self):
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag5 = False
        flag6 = False
        while not (flag1 & flag2 & flag3 & flag4 & flag5 & flag6):
            username = input("Username: ").strip()
            firstname = input("First name: ").strip()
            lastname = input("Last name: ").strip()
            email = input("Email: ").strip()
            age = input("Age: ")
            password = input("Password: ").strip()
            retype_password = input("Re-type password: ").strip()

            if username == '':
                print("username should be filled.")
                flag1 = False
            else:
                flag1 = True
    
            flag2 = True
            for user in self.userlist:
                if user.username == username:
                    print("Username was already been taken. Please choose another name.")
                    flag2 = False
                    break
                else:
                    flag2 = True
    
            if firstname == '':
                print("First name should not be blank.")
                flag3 = False
            else:
                flag3 = True
    
            if lastname == '':
                print("Last name should not be blank.")
                flag4 = False
            else:
                flag4 = True
                
            if email == '':
                print("Email should not be blank.")
                flag5 = False
            else:
                flag5 = True
    
            if (len(password) < 6) or (retype_password != password):
                print("Password is incorrect.")
                flag6 = False
            else:
                flag6 = True
    
        self.userlist.append(User(firstname, lastname, username, email, password, age))
        print("New user has been created.")
        
    def list_all_user(self):
        print('There are {} user.'.format(len(self.userlist)))
        for user in self.userlist:
            print('{}'.format(user))
    
    def logout(self, current_user):
        current_user = None
        self.isLogin = False
        print('Logged out!!!')
    
    def upgrage(self):
        pass