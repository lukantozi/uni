import random


def user_inp():
    flag = False
    num_low = 0
    num_high = 0
    while flag == False:
        try:
            num_low = int(input("Please enter a number between 1 and 9: "))
        except ValueError:
            print("Only integers are allowed!")
            continue
        if num_low < 1 or num_low > 9:
            print("Range: 1-9")
            continue
        flag = True

    flag = False
    while flag == False:
        try:
            num_high = int(input("Please enter a number between 10 and 100: "))
        except ValueError:
            print("Only numeric characters are allowed!")
            continue
        if num_high < 10 or num_low > 100:
            print("Range: 10-100")
            continue
        flag = True

    comp_num =  random.randint(num_low, num_high)
    return comp_num


def guess_num():
    flag = False
    guess = 0
    while flag == False:
        try: 
            guess = int(input("I am thikning of a number...\n~"))
            flag = True
        except ValueError:
            print("Please only enter integer values")
    return guess


def compare(num):
    flag = False
    while flag == False:
        guessed = guess_num()
        if guessed > num:
            print("Too high, try again...")
            continue
        elif guessed < num:
            print("Too low, try again...")
        else:
            print("You win!")
            flag = True
    return 0

def main():
    val = user_inp()
    compare(val)


main()
