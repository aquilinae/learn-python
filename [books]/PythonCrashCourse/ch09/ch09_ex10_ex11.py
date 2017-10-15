from ch09_ex10_restaraunt import Restaurant
from ch09_ex11_user import Admin

# Task 10

print("\n# TASK 10\n")

samovar = Restaurant("Samovar", "Russian")
samovar.describe_restaurant()

# Task 11

print("\n# TASK 11\n")

anykey = Admin("Andrei", "Anykeev")
anykey.describe_user()
anykey.privilleges.show_privilliges()
