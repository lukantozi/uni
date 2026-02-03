import random


def main():
    num = random.randint(1,5)
    user_guess = validate_integer()
    if user_guess > num:
        print("Too high, try again\n~ ")
        user_guess = validate_integer()
    elif user_guess < num:
        print("Too low, try again\n~ ")
        user_guess = validate_integer()
    else:
        print("Well done")

    if user_guess == num:
        print("Correct")
        return
    else:
        print("You lose")
        return

def validate_integer():
    while True:
        try:
            user_guess = int(input("Pick a number between 1 and 5\n~ "))
            return user_guess
        except ValueError:
            print("Please enter an integer.\n")

if "__main__" == __name__:
    main()
