numbers = [321, 198, 853, 459]

while True:
    try:
        user_choice = int(input("Enter a three digit number: "))
        break
    except ValueError:
        print("Please enter a number")

if user_choice in numbers:
    print(numbers.index(user_choice))
else:
    print("That is not in the list")
