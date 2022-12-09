#3-1 Names:
names = ['Arvin','Alex','Naty']

print(names[0])
print(names[1])
print(names[2])

#3.2 Greetings:
names = ['Arvin','Alex','Naty']

print(f"Hi! {names[0]}")
print(f"Hi! {names[1]}")
print(f"Hi! {names[2]}")

#3.3 Your Own List:
names = ['Honda','BMW','Tesla']

print(f"I would like a {names[0]} motorcycle.")
print(f"I wound like a {names[1]} car.")
print(f"I wound like a {names[2]} car.")

#3.4 Guest List:
names = ['Arvin', 'Alex', 'Naty']

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.")

#3.5 Changing Guest List
names = ['Arvin', 'Alex', 'Naty']

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.")

print(f"{names.pop(0)} can't come to the party.")
print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")

#3.6 More Guests
names = ['Arvin', 'Alex', 'Naty']

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.\n")

print(f"{names.pop(0)} can't come to the party.\n")
print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.\n")

print(f"I've found a bigger table, {names[0]} and {names[1]}.\n")
names.insert(0, 'Oishi')
names.insert(2, 'Pringle')
names.append('Chippy')

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.")
print(f"Please come to the party {names[3]}.")
print(f"Please come to the party {names[4]}.\n")

#3.7 Shrinking Guest List:
names = ['Arvin', 'Alex', 'Naty']

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.\n")

print(f"{names.pop(0)} can't come to the party.\n")
print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.\n")

print(f"I've found a bigger table, {names[0]} and {names[1]}.\n")
names.insert(0, 'Oishi')
names.insert(2, 'Pringle')
names.append('Chippy')

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.")
print(f"Please come to the party {names[2]}.")
print(f"Please come to the party {names[3]}.")
print(f"Please come to the party {names[4]}.\n")

print("Sorry, I can only invite two people.\n")
names.pop()
names.pop()
names.pop()

print(f"Please come to the party {names[0]}.")
print(f"Please come to the party {names[1]}.\n")

del names[0]
del names[0]

print(names)

#3.8 Seeing the World:
locations = ['Philippines', 'USA', 'Japan','Korea','Spain']

print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations,reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#3.9 Dinner Guests:
names = ['Arvin','Alex','Naty']

print(len(names))

#3.10 Every Function:
names = []

names.insert(0, 'Arvin')
names.append('Alex')
names.insert(1, 'Naty')

print(names)

