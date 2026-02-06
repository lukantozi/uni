from random import randint

def three_exceptions():
    operations = [
        lambda: int("abc"),
        lambda: 10 / 0,
        lambda: [1][5]
    ]
    
    for op in operations:
        try:
            op()
        except ValueError:
            print("ValueError caught")
        except ZeroDivisionError:
            print("ZeroDivisionError caught")
        except IndexError:
            print("IndexError caught")


def validate_email():
    flag = True
    email = None
    while flag:
        try:
            email = input("Please enter your email: ")
            for char in email:
                if char == '@':
                    flag = False
                    break
            if flag:
                raise ValueError("email must contain '@'")
        except ValueError as e:
            print(e)
    return "email validated" 

#print(validate_email())

def catch_exception():
    try:
        x = int(input("Enter number: "))
        result = 10 / x
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")

def valid_num():
    num = randint(1, 100)

    flag = True
    while flag:
        try:
            guess = int(input("enter the number: "))
            if guess > num:
                raise ValueError("too high")
            elif guess < num:
                raise ValueError("too low")
            flag = False
        except ValueError as e:
            print(e)
    print("you've guessed the number!")
#valid_num()

def else_exception():
    for n in range(10):
        div = randint(0, 1)
        try:
            res = n / div
        except ZeroDivisionError:
            print("can't divide by 0")
        else:
            print(res)
#else_exception()
