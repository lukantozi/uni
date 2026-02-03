import random

def main():
    num = random.randint(1,10)
    user_guess = validate_integer()
    while True:
        if user_guess < num:
            print("\nToo low, try again.\n")
            user_guess = validate_integer()
            continue
        elif user_guess > num:
            print("\nToo high, try again.\n")
            user_guess = validate_integer()
            continue
        else:
            print("Well done!")
            break


def validate_integer():
    while True:
        try:
            user_guess = int(input("\nPick a number between 1 and 10\n~ "))
            validate_range(user_guess)
            return user_guess
        except ValueError:
            print("\nPlease enter an integer.\n")


def validate_range(num):
    while True:
        if num > 10:
            print("Number should be equal or less than 10")
            num = validate_integer() 
            continue
        elif num < 1:
            print("Number should be equal or greater than 1")
            num = validate_integer()
            continue
        return

if "__main__" == __name__:
    main()

