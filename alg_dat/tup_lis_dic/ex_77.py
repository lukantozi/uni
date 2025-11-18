names = []
for _ in range(3):
    names.append(input("Enter the name of the person you would like to invite: "))

count = 3

while True:
    add_another = input("\nWould you like to invite more people? [yes/no]\n~ ").lower()
    if add_another in ["yes", "y"]:
        count += 1
        names.append(input("Enter the name of the person you would like to invite: "))
        continue
    elif add_another in ["no", "n"]:
        break
    else:
        print("\nPlease answer with [yes/y] or [no/n]\n")
        continue

while True:
    name = input(f"Type one of the names on the list: {names}\n~ ").lower()
    if name in names:
        ind = names.index(name)
        print(ind)
        break
    else:
        print("That name is not on the list")


while True:
    still_coming = input(f"Would you still like {names[ind].title()} to come to party? [yes/no]\n~ ").lower()
    if still_coming in ["yes", "y"]:
        break
    elif still_coming in ["no", "n"]:
        names.remove(name)
        break
    else:
        print("\nPlease answer with [yes/y] or [no/n]\n")

print(names)
