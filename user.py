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
        if self.userid is None:
            self.userid = "user" + ('00' if User.count < 10 else '0' if User.count < 100 else '') + str(User.count)
        else:
            self.userid = userid
        self.username = username
        self.email = email
        self.password = encode_string(password)
        self.age = age
        self.booksBorrowed = []
        self.noBooksBorrowed = 0

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
        print("Age: Unknown") if self.age is None else print("Age: {} years old".format(str(self.age)))
        print("Right: Admin.") if self.prior == 2 \
            else (print("Right: Moderator.") if self.prior == 1 else print("Right: Normal user."))
        print("-------------------------------------------------------------")
        return 1

    @classmethod
    def requestBook(self):
        bookisbn = input("Enter the isbn of the book you'd like to borrow>>")
        return bookisbn

    def showBooksBorrowed(self):
        return self.booksBorrowed

    def edit_booksBorrowed(self, isbn):
        self.booksBorrowed.append(isbn)

    def returnBook(self):
        print("Enter the isbn of the book you'd like to return>>")
        self.bookisbn = input()
        if self.bookisbn in(self.booksBorrowed):
            self.noBooksBorrowed -= 1
            self.booksBorrowed.remove(self.bookisbn)
            return self.bookisbn
        return None

    def __repr__(self):
        return type(self).__name__ + '({}, {})'.format(self.userid, self.username)

    def __str__(self):
        return '{} - {} - {} {} - {} - {} - ({})'\
                        .format(self.userid,
                                self.username,
                                self.firstname, self.lastname,
                                self.email,
                                self.age,
                                type(self).__name__)

    def userUp2Mod(self):
        self.__class__ = Moderator
        print("User {} has been upgraded to Moderator.".format(self.userid))


class Admin(User):
    prior = 2

    def __init__(self, firstname, lastname, username, email, password, age=None, userid=None):
        super().__init__(firstname, lastname, username, email, password, age, userid)

    def adminDown2Mod(self):
        self.__class__ = Moderator
        print("Admin {} has been downgraded to Moderator.".format(self.userid))

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

    def modUp2Admin(self):
        self.__class__ = Admin
        print("Moderator {} has been upgraded to Admin.".format(self.userid))

    def modDown2User(self):
        self.__class__ = User
        print("Moderator {} has been downgraded to Normal user.".format(self.userid))

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

    def upgrade_downgrade_user(self, current_user, p_useid, updown):
        exit = True
        for i_user in self.userlist:
            if i_user.userid == p_useid:
                index = self.userlist.index(i_user)
                exit = False
                break
        if not exit:
            if updown == "up":
                if i_user.prior == 0:
                    self.userlist[index].userUp2Mod()
                elif i_user.prior == 1:
                    self.userlist[index].modUp2Admin()
                elif i_user.prior == 2:
                    print('User {} is Admin already.'.format(p_useid))
            elif updown == "down":
                if i_user.prior == 1:
                    self.userlist[index].modDown2User()
                elif i_user.prior == 2:
                    self.userlist[index].adminDown2Mod()
                elif i_user.prior == 0:
                    print('User {} is Normal user already.'.format(p_useid))
        else:
            print('User {} is not found.'.format(p_useid))

    def logout(self, current_user):
        current_user = None
        self.isLogin = False
        print('Logged out!!!')
    
    def upgrage(self):
        pass