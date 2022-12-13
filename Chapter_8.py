#8-1 Message:
def display_message():
    print("I'm learning about functions!")

display_message()

#8-2 Favorite Book:
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Andrew Tate's Mantra")

#8-3 T-Shirt:
def make_shirt(size,text):
    print(f'The size of the shirt is {size} with printed text "{text}".')

make_shirt('Large',text="HEHE!")

#8-4 Large Shirts:
def make_shirt(text="I love PYTHON!",size = 'Large'):
    print(f'The size of the shirt is {size} with printed text "{text}".')

make_shirt()

#8-5 Cities:
def describe_city(city,country = 'Philippines'):
    print(f"{city} is in {country}.")

describe_city('Quezon City')

#8-6 City Names:
def city_country(city, country):
    formatted_text = f"{city}, {country}"
    return formatted_text.title()

print(city_country('quezon city','philippines'))
print(city_country('osaka','japan'))
print(city_country('madrid','spain'))

#8-7 Album:
pack = {}
def make_album(album,singer):
    pack[singer] = album
    return pack
make_album('Songs about Jane','Maroon 5')
make_album('Sheesh','Shoosh')
print(pack)

#8-8 User Albums:
def make_album(album,singer):
    pack = {singer:album}
    print(pack)

while True:
    si = input("Enter the singer's name: ")
    al = input("Enter the album's name: ")
    make_album(al,si)

    check = input ("Do you want to add more? (Yes/No)")
    if check == "No":
        break

#8-9 Messages:
def show_messages(messages):
    for message in messages:
        print(message)

text = ['Love is blind!','Money is power!']
show_messages(text)

#8-10 Sending Messages:
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,nmessages):
    while messages:
        me = messages.pop()
        print(f"Sending {me}.")
        nmessages.append(me)   

text = ['Love is blind!','Money is power!']
newtext = []

show_messages(text)
send_messages(text,newtext)
print(text)
print(newtext)

#8-11 Archived Messages:
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages,nmessages):
    while messages:
        me = messages.pop()
        print(f"Sending {me}.")
        nmessages.append(me)   

text = ['Love is blind!','Money is power!']
newtext = []

show_messages(text)
send_messages(text[:],newtext)
print(text)
print(newtext)

#8-12 Sandwiches:
def create_sandwich(*toppings):
    for top in toppings:
        print(f"Adding {top} toppings.")

create_sandwich('Ham','Egg')
create_sandwich('Cheese','Bacon')

#8-13 Build Profile:
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Arvin', 'Mayapis',
                                location='QC',
                                field='technology')
print(user_profile)

#8-14 Cars:
def make_car(brand,model,**addons):
    addons['Brand'] = brand
    addons['Model'] = model
    return addons
make = make_car('Foton','Beast',speed='slow',color='black')
print(make)

#8-15 Printing Models:

#8-16 Imports:

#8-17 Styling Functions: