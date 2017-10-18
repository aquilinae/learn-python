class User():

    def __init__(self, fname, lname, phone='No phone', email='No e-mail'):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("User name is", self.fname.title(), self.lname.title())
        print("Phone:", self.phone, "\te-mail:", self.email.lower())

    def greet_user(self):
        print("\nGreetings,", self.fname, self.lname)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privilleges():

    def __init__(self, privilleges):
        self.privilleges = privilleges

    def show_privilliges(self):
        for privillege in self.privilleges:
            print(privillege.capitalize())

class Admin(User):

    def __init__(self, fname, lname, phone='No phone', email='No e-mail'):
        super().__init__(fname, lname, phone, email)
        self.privilleges = Privilleges(privilleges)

privilleges = [
    "delete users",
    "add users",
    "create spaces",
    "managing boards",
    ]
