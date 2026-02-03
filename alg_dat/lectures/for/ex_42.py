total = 0
for _ in range(5):
    number = int(input("Enter the number: "))
    while True:
        resp = input("Would you like to add this number to total? [yes/no]: ").lower()
        if resp in ["y", "ye", "yes"]:
            total = total + number
            break
        elif resp in ["n", "no"]:
            break
        else:
            print("Please answer with yes/no.")
            continue
print(total)
