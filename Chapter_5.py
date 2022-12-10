#5-1 Conditional Tests:
food = 'noodles'
print("Is food == 'noodles'? I predict True.")
print(food == 'noodles')

print("\nIs food == 'chicken'? I predict False.")
print(food == 'chicken')

#5-2 More Conditional Tests:
print(f"1 > 2 = {1>2}")
print(f"9 < 11 = {9<11}")
print(f"6 != 9 = {6!=9}")

#5-3 Alien Colors #1:
alien_color = 'red'

if alien_color == 'red':
    print("You just earned 5 points!")

if alien_color == 'gren':
    print("You just earned 5 points!")
else:
    print("Warning!")

#5-4 Alien Colors #2:
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#5-5 Alien Colors #3:
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
elif alien_color == 'red':
    print("You just earned 15 points!")

#5-6 Stages of Life:
age = 69

if age < 2:
    print("You are a baby!")
elif age > 2 and age < 4:
    print("You are a toddler!")
elif age > 4 and age < 13:
    print("You are a kid!")
elif age > 13 and age < 20:
    print("You are a teenager!")
elif age > 20 and age < 65:
    print("You are an adult!")
else:
    print("You are an elder!")

#5-7 Favorite Fruit:
favorite_fruits = ['apple','strawberry','orange']

if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")

#5-8 Hello Admin:
username = ['admin','user','main','nicolas','arvin']

for name in username:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again.")

#5-9 No Users:
username = []

if username:
    print("Hello Users!")
else:
    print("We need to find some users!")

#5-10 Checking Usernames:
current_users = ['arvin','nicolas','alex','naty','red']
new_users = ['john','russel','arvin','nicolas','jack']

for name in new_users:
    if name in current_users:
        print(f"{name} is currently in use! Enter new username.")
    else:
        print(f"{name} is available!")

#5-11 Ordinal Numbers:
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif number == 1:
        print(f"{number}st")
    else:
        print(f"{number}th")

#5-12 Styling if statements:

#5-13 Your Ideas:



