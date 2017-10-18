# Task 6

print("\n# TASK 6\n")

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is", self.restaurant_name)
        print("It have", self.cuisine_type, "kitchen!")

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors (self):
        for flavor in self.flavors:
            print(flavor.title())

flavors = ["bacon ice cream", "blue moon", "cherry ice cream",
    "chocolate ice cream", "grape ice cream", "peppermint ice cream",
    "pistachio ice cream", "strawberry ice cream", "tutti frutti",
    "vanilla ice cream"]

baskin_robbins = IceCreamStand("Baskin Robbins", "Ice Cream", flavors)

baskin_robbins.show_flavors()

# Task 7

print("\n# TASK 7\n")

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

class Admin(User):

    def __init__(self, fname, lname, privilleges, phone='No phone', email='No e-mail'):
        super().__init__(fname, lname, phone, email)
        self.privilleges = privilleges

    def show_privilliges(self):
        print(self.fname, self.lname, "is able to:")
        for privillege in self.privilleges:
            print(privillege.capitalize())

privilleges = [
    "delete users",
    "add users",
    "create spaces",
    "managing boards",
    ]

anykey = Admin("Andrei", "Deploev", privilleges, "79877891266")
anykey.show_privilliges()
anykey.describe_user()

# Task 8

print("\n# TASK 8\n")

class Privilleges():

    def __init__(self, privilleges):
        self.privilleges = privilleges

    def show_privilliges(self):
        for privillege in self.privilleges:
            print(privillege.capitalize())

privilleges = [
    "add users",
    "managing boards",
    ]

class Admin(User):

    def __init__(self, fname, lname, phone='No phone', email='No e-mail'):
        super().__init__(fname, lname, phone, email)
        self.privilleges = Privilleges(privilleges)

keyany = Admin("Valerii", "Undeploev", "79877891266")

keyany.privilleges.show_privilliges()
