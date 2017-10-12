class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is", self.restaurant_name)
        print("It have", self.cuisine_type, "kitchen!")

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")

    def set_number_server(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

class User():

    def __init__(
        self,
        first_name, last_name, phone='No phone', email='No e-mail', company ='Unemployed'):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.company = company
        self.login_attempts = 0

    def describe_user(self):
        print("We have a person called", self.first_name.title(), self.last_name.title())
        print("His/er phone is", self.phone, "and e-mail is", self.email)
        print("He/she works at", self.company)

    def greet_user(self):
        print("Greetings,", self.first_name, self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# Task 4.1
restaurant = Restaurant("Blue Oyster", "French")
print("Number of served customers is:", restaurant.number_served)
restaurant.number_served = 8
print("Number of served customers is:", restaurant.number_served)

# Task 4.2
restaurant.set_number_server(12)
print("Number of served customers is:", restaurant.number_served)

# Task 4.3
restaurant.increment_number_served(5)
print("Number of served customers is:", restaurant.number_served)
restaurant.increment_number_served(1)
print("Number of served customers is:", restaurant.number_served)

print()

# Task 5
nikolai = User('Nikolai', 'Nikolaev', '7887774488', 'nikolai@monkeybusiness.com', 'Monkey Business LLC')
ivan = User('Ivan', 'Ivanov')
nikolai.describe_user()
print("Number of", nikolai.first_name, "login attempts is:", nikolai.login_attempts)
ivan.describe_user()
print("Number of", ivan.first_name, "login attempts is:", ivan.login_attempts)

nikolai.increment_login_attempts()
print("Number of", nikolai.first_name, "login attempts is:", nikolai.login_attempts)
ivan.increment_login_attempts()
print("Number of", ivan.first_name, "login attempts is:", ivan.login_attempts)
ivan.increment_login_attempts()
print("Number of", ivan.first_name, "login attempts is:", ivan.login_attempts)

ivan.reset_login_attempts()
print("Number of", ivan.first_name, "login attempts is:", ivan.login_attempts)
