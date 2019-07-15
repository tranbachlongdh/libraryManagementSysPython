class User:
    prior = -1
    count = 0

    def __init__(self, firstname, lastname, username, email, password, age=None):
        User.count += 1
        self.firstname = firstname
        self.lastname = lastname
        self.userid = "user" + ('00' if User.count<10 else '0' if User.count<100 else '') + str(User.count)
        self.username = username
        self.email = email
        self.password = password
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
        self.password = update_password

    def show_userInfo(self):
        print("-------------------------------------------------------------")
        print("User ID: " + str(self.userid))
        print("User name: " + str(self.username))
        print("Email: " + str(self.email))
        print("Full name: {} {}".format(str(self.firstname), str(self.lastname)))
        print("Age: Unknown") if self.age == None else print("Age: {} years old".format(str(self.age)))
        print("Right: Admin.") if self.prior == 1 else print("Right: Normal user.")
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
        return type(self).__name__ + ': ID({}) --- Username({})'.format(self.userid, self.username)


class Admin(User):

    def __init__(self, firstname, lastname, username, email, password, age=None):
        super().__init__(firstname, lastname, username, email, password, age)
        self.prior = 1

    def add(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


# user1 = Admin("Long", 'Tran', 'rose4u', 'tranbachlongdh@gmail.com', 'youaremyHero#1', 20)
# user1.show_userInfo()
# print(user1)