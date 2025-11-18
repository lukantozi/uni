names = []
for _ in range(3):
    names.append(input("Enter the name of the person you would like to invite: "))


while True:
    add_another = input("Would you like to invite more people? [yes/no]\n~ ").lower()
    if add_another in ["yes", "y"]:
        names.append(input("Enter the name of the person you would like to invite: "))
        continue
    elif add_another in ["no", "n"]:
        break
    else:
        print("\nPlease answer with [yes/y] or [no/n]\n")
        continue

print(f"You have invited {len(names)} people to the party")

