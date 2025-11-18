countries = ("poland", "germany", "france", "spain", "portugal")
while True:
    try:
        number = int(input(f"Pick a number between 1-5\n~ "))
        break
    except ValueError:
        print("Please enter a number")

print(countries[number-1])

