#9-1 Restaurant:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

one = Restaurant("David's Tea House","Chinese")

one.describe_restaurant()
one.open_restaurant()

#9-2 Three Restaurants:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

one = Restaurant("David's Tea House","Chinese")
two = Restaurant("Jollibee","Filipino")
three = Restaurant("Chowking",'Chinese')

one.describe_restaurant()
two.describe_restaurant()
three.describe_restaurant()

#9-3 Users:
class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} - {self.last_name} - {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

cardo = Users('Cardo','Dalisay','69')
cardo.describe_user()
cardo.greet_user()

#9-4 Number Served:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self,number):
        self.number_served = number
        print(f"Total number serve: {self.number_served}")

    def increment_number_served(self):
        self.number_served += 10
        print(f"Total number serve: {self.number_served}")

one = Restaurant("David's Tea House","Chinese")

one.set_number_served(10)
one.increment_number_served()

#9-5 Login Attempts:
class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} - {self.last_name} - {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attemps(self):
        self.login_attempts = 0
    
cardo = Users('Cardo','Dalisay','69')
cardo.describe_user()
cardo.greet_user()
cardo.increment_login_attemps()
print(cardo.login_attempts)
cardo.reset_login_attemps()
print(cardo.login_attempts)

#9-6 Ice Cream Stand:
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} - {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

one = Restaurant("David's Tea House","Chinese")

one.describe_restaurant()
one.open_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def printFlavors(self):
        for flavor in self.flavors:
            print(flavor)

cream = IceCreamStand('Dairy Queen','Desserts',['Oreo','Buttercup','Mango'])
cream.printFlavors()

#9-7 Admin:
class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} - {self.last_name} - {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

cardo = Users('Cardo','Dalisay','69')
cardo.describe_user()
cardo.greet_user()

class Admin(Users):
    def __init__(self, first_name, last_name, age,privilages):
        super().__init__(first_name, last_name, age)
        self.privilages = privilages
    
    def show_privilages(self):
        for privilage in self.privilages:
            print(privilage)

method = Admin('Red','Vanz','12',['Wew','Wow','Wowowee'])
method.show_privilages()

#9-8 Privileges:
class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"{self.first_name} - {self.last_name} - {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

class Admin(Users):
    def __init__(self, first_name, last_name, age,privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

move = Admin('Red','Black','12',['Wow','wow','win'])
Privileges.show_privileges(move)

#9-9 Battery Upgrade:

#9-10 Imported Restaurant:

#9-11 Imported Admin:

#9-12 Multiple Modules:

#9-13 Dice:
from random import randint
def roll_dice(sides = 6):
    number  = randint(1,sides)
    return number

print(roll_dice())

#9-14 Lottery:
from random import choice

series = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']

def roll_dice(serie):
    one  = choice(serie)
    two  = choice(serie)
    three  = choice(serie)
    four  = choice(serie)
    return f" {one} - {two} - {three} - {four}: Winning Ticket (Any Combinations)"

print(roll_dice(series))

#9-15 Lottery Analysis:
from random import choice

series = [1,2,3,4,5,6,7,8,9,10,'A','B','C','D','E']
my_ticket = [9,'A',6,'C']
counter = 0
def roll_dice(serie):
    one  = choice(serie)
    two  = choice(serie)
    three  = choice(serie)
    four  = choice(serie)
    set = [one,two,three,four]
    return set

while True:
    test = roll_dice(series)
    if my_ticket == test:
        break
    else:
        counter += 1

print(counter)

#9-16 Python Module of the Week:



