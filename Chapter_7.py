#7-1 Rental Car:
car = input("What kind of rental car would you like?: ")

print(f"Let me see if I can find you a {car}.")

#7-2 Restaurant Seating:
seating = int(input("How many are you?: "))

if seating > 8:
    print("You'll have to wait for a table.")
else:
    print("The table is ready. Come this way.")

#7-3 Multiples of Ten:
number = int(input("Give me a number: "))

if number % 10 == 0:
    print("The number is a multiple of ten.")
else:
    print("The number is not a multiple of ten.")

#7-4 Pizza Toppings:
while True:
    check = input("Enter a topping: ")
    if check == 'quit':
        print("Pizza is getting ready.")
        break
    else:
        print(f"Adding {check} topping.")

#7-5 Movie Tickets:
while True:
    age = int(input("Enter your age: "))
    if age < 3:
        print("The ticket is free!")
    elif 12 >= age >= 3:
        print("The ticket is 10$")
    else:
        print("The ticket is 15$")

#7-6 Three Exits:
while True:
    check = input("Enter a topping: ")
    if check == 'quit':
        print("Pizza is getting ready.")
        break
    else:
        print(f"Adding {check} topping.")

active = True
while active:
    check = input("Enter a topping: ")
    if check == 'quit':
        print("Pizza is getting ready.")
        active = False
    else:
        print(f"Adding {check} topping.")
        
check = ""
while check!='quit':
    check = input("Enter a topping: ")
    print(f"Adding {check} topping.")
print("Pizza is getting ready.")

#7-7 Infinity:
while True:
    print("HEHE!")

#7-8 Deli:
sandwich_orders = ['ham','egg','chicken','hotdog','bacon']
finished_sandwiches = []

while sandwich_orders:
    move = sandwich_orders.pop()
    print(f"I made your {move} orders.")
    finished_sandwiches.append(move)

for food in finished_sandwiches:
    print(f"{food} sandwich is made.")

#7-9 No Pastrami:
sandwich_orders = ['ham','egg','chicken','hotdog','bacon','pastrami']
finished_sandwiches = []
print("Deli has run out of Pastrami!")
while sandwich_orders:
    move = sandwich_orders.pop()
    if move == 'pastrami':
        continue
    else:
        print(f"I made your {move} orders.")
        finished_sandwiches.append(move)

for food in finished_sandwiches:
    print(f"{food} sandwich is made.")

#7-10 Dream Vacation:
vacation = {}

while True:
    name = input("What is your name? ")
    place = input("Where is your dream vacation? ")
    question = input("Would you like add another response? (yes / no) ")
    vacation[name] = place
    if question == 'no':
        break
        
for fname, nplace in vacation.items():
    print(f"{fname} would like to go to {nplace}")


