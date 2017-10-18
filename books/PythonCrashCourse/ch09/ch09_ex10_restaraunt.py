class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is", self.restaurant_name)
        print("It have", self.cuisine_type, "kitchen!")

    def open_restaurant(self):
        print(self.restaurant_name, "is open!")
