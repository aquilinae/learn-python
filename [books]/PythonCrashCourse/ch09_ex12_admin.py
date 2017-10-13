from ch09_ex12_user import User

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
    "changing roles"
    ]
