import random


def choice():
    flag = False
    oper = 0
    while flag == False:
        try:
            oper = int(input("1) Addition\n2) Subtraction\nEnter 1 or 2: "))
            flag = True
        except ValueError:
            print("Please choose by entering 1 or 2")
    return oper


def addition():
    num_1 = random.randint(5, 20)
    num_2 = random.randint(5, 20)
    answer = 0
    flag = False
    while flag == False:
        try:
            answer = int(input(f"{num_1} + {num_2} = "))
        except ValueError:
            print("Please enter an integer!")
            continue
        if answer == num_1 + num_2:
            print("Correct!")
            flag = True
        else:
            print("Wrong, try again...")


def subtraction():
    num_1 = random.randint(25, 50)
    num_2 = random.randint(1, 25)
    flag = False
    answer = 0
    while flag == False:
        try:
            answer = int(input(f"{num_1} - {num_2} = "))
        except ValueError:
            print("Please enter an integer!")
            continue
        if answer == num_1 - num_2:
            print("Correct!")
            flag = True
        else:
            print("Wrong, try again...")


def main():
    operation = choice()
    if operation == 1:
        addition()
    elif operation == 2:
        subtraction()


main()
