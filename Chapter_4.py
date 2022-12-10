#4-1 Pizzas:
pizza = ['Hawaiian',"Meat-lover",'Overload']

for name in pizza:
    print(f"I like {name} pizza.")

print("I really love pizza!")

#4-2 Animals:
pets = ['dog',"cat",'bird']

for name in pets:
    print(f"A {name} would make a great pet.")

print("Any of these animals would make a great pet!")

#4-3 Counting to Twenty:
for number in range(1,21):
    print(number)

#4-4 One Million:
numbers = []

for number in range (1,1000001):
    numbers.append(number)
    print(number)

#4-5 Summing a Million:
numbers = []

for number in range (1,1000001):
    numbers.append(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4.6 Odd Numbers:
for number in range (1,20,2):
    print(number)

#4.7 Threes:
for number in range (3,33,3):
    print(number)

#4.8 Cubes:
for number in range (1,11):
    print(number**3)

#4.9 Cube Comprehension:
cubes = [value**3 for value in range(1,11)]
print(cubes)

#4.10 Slices:
names = ['Arvin','Nicolas','Alex','Naty','Red']

for name in names[:3]:
    print(f"Hello, {name}!")

for name in names[1:4]:
    print(f"Hi, {name}!")

for name in names[2:]:
    print(f"Bonjour, {name}!")

#4.11 My Pizzas, Your Pizzas:
pizza = ['Hawaiian',"Meat-lover",'Overload']
friend_pizza = pizza[:]

for name in pizza:
    print(f"I like {name} pizza.")

friend_pizza.append('Vegan')
friend_pizza.append('Ham & Cheese')

for name in friend_pizza:
    print(f"My friend's favourite pizzas are {name}.")

#4-12 More loops:
pizza = ['Hawaiian',"Meat-lover",'Overload']
friend_pizza = pizza[:]

print("My favourite pizzas:")
for name in pizza:
    print(f"{name}")

friend_pizza.append('Vegan')
friend_pizza.append('Ham & Cheese')

print("My Friend's favourite pizzas:")
for name in friend_pizza:
    print(f"{name}")

#4-13 Buffet:
foods = ('Beef','Chicken','Pork','Seafoods','Vegan')

print("Available foods in the restaurant:")
for food in foods:
    print(food)

foods = ('Beef','Chicken','Pork','Dog','Lamb')

print("Available foods in the restaurant:")
for food in foods:
    print(food)
