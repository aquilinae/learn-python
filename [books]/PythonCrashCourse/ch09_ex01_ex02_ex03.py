class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is", self.restaurant_name)
        print("It have", self.cuisine_type, "kitchen!")

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")

# Task 1
print("Task 1")
restaurant = Restaurant("McDonalds", "American")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()

# Task 2
french = Restaurant("Blue Oyster", "French")
russian = Restaurant("Red Hammer", "Russian")
chiniese = Restaurant("Chong Quai Ngmai", "Chiniese")
french.describe_restaurant()
russian.describe_restaurant()
chiniese.describe_restaurant()


class User():

    def __init__(self, first_name, last_name, phone, email, company):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.company = company

    def describe_user(self):
        print("We have a person called", self.first_name.title(), self.last_name.title())
        print("His/er phone is", self.phone, "and e-mail is", self.email)
        print("He/she works at", self.company)

    def greet_user(self):
        print("Greetings,", self.first_name, self.last_name)

nikolai = User('Nikolai', 'Nikolaev', '7887774488', 'nikolai@gmail.com', 'Monkey Business LLC')
petr = User('Petr', 'Petrov', '79877894578', 'petrov@gmail.com', 'Ulsoft')
ivan = User('Ivan', 'Ivanov', '79845789941', 'vanya@gmail.com', 'Rapid Platfrom')

nikolai.describe_user()
nikolai.greet_user()
petr.describe_user()
petr.greet_user()
ivan.describe_user()
ivan.greet_user()
