import random


def main():
    num = random.randint(1,10)
    user_guess = validate_integer()
    while True:
        if user_guess != num:
            print("Wrong guess, try again.\n")
            user_guess = validate_integer()
            continue
        else:
            print("Well done")
            break


def validate_integer():
    while True:
        try:
            user_guess = int(input("Pick a number between 1 and 10\n~ "))
            return user_guess
        except ValueError:
            print("Please enter an integer.\n")

if "__main__" == __name__:
    main()
