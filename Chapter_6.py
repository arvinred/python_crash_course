#6-1 Person:
bio = {'first_name':'Arvin',
        'last_name':'Mayapis',
        'Age':25,'City':'Quezon City'}

print(bio['first_name'])
print(bio['last_name'])
print(bio['Age'])
print(bio['City'])

#6-2 Favorite Numbers:
numbers = {'Arvin':9,'Alex':19,'Naty':27}

print(numbers['Arvin'])
print(numbers['Alex'])
print(numbers['Naty'])

#6-3 Glossary:
glossary = {'Variable':'Use to store values','String':'A character variable',}

print(f"Variable \n{glossary['Variable']}")
print(f"String \n{glossary['String']}")

#6-4 Glossary 2:
glossary = {'Variable':'Use to store values','String':'A character variable',}

for name,meaning in glossary.items():
    print(f"{name} - {meaning}")

#6-5 Rivers:
river = {'Nile':'Egypt','Amazon':'Peru','Yangtze':'China'}

for name,country in river.items():
    print(f"The {name} runs through {country}.")

#6-6 Polling:
poll = {'Arvin':'Yes','Alex':'No','Naty':'No'}

for name,done in poll.items():
    if done == 'No':
        print(f"{name}, please answer the poll.")
    else:
        print(f"Thank you answering the poll, {name}.")

#6-7 People:
bio = {'first_name':'Arvin',
        'last_name':'Mayapis',
        'Age':25,'City':'Quezon City'}

for name,info in bio.items():
    print(f"{name} : {info}")

#6-8 Pets:
bird = {'Animal':'Bird', 'Color':'White'}
dog = {'Animal':'Dog','Color':'Black'}
cat = {'Animal':'Cat','Color':'Orange'}

pets = [bird,dog,cat]

for info in pets:
    print(f"Animal : {info['Animal']} \nColor : {info['Color']}")

#6-9 Favorite Places:
favorite_places = {'Arvin':['House','Library'],'Alex':['SM','Robinson'],'Naty':['SM','Cinema']}

for name,places in favorite_places.items():
    print(f"{name}'s Favorite Places:")
    for place in places:
        print(place)

#6-10 Favorite Numbers:
numbers = {'Arvin':9,'Alex':19,'Naty':27}

for name,number in numbers.items():
    print(f"{name}'s favorite number is {number}.")

#6-11 Cities:
cities = {
    'Quezon City':
    {
        'People' : 'Mix',
        'Population' : '100'
    },
    'Manila City':
    {
        'People' : 'Tagalog',
        'Population' : '500'
    },
    'Cebu City':
    {
        'People' : 'Bisaya',
        'Population' : '200'
    },
}

for city,info in cities.items():
    print(city)
    print(f"The people are {info['People']}")
    print(f"The population count is {info['Population']}")

#6-12 Extensions:
