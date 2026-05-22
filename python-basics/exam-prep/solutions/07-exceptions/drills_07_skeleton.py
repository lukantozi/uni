from random import randint

def division():
    a = 0
    b = 0
    div = 0

    flag = True
    main_flag = True
    while main_flag:
        while flag:
            try:
                a = int(input("Please enter the first number: "))
                flag = False
            except ValueError:
                print("Please enter only integers")

        flag = True
        while flag:
            try:
                b = int(input("Please enter the second number: "))
                flag = False
                try:
                    div = a / b
                    main_flag = False
                except ZeroDivisionError:
                    print("Can't divide by 0")
            except ValueError:
                print("Please enter only integers")

    return div

#print(division())

def validate_password():
    flag = True
    psswd = None

    while flag:
        try:
            psswd = input("Please enter your password: ")
            n = len(psswd)

            if n < 8:
                raise ValueError("Password should be minimum 8 characters") 
            elif n > 12:
                raise ValueError("Password should be maximum 12 characters") 

            if psswd == psswd.lower():
                raise ValueError("Password must contain at least one capital letter")
            flag = False

        except ValueError as e:
            print(e)
    return psswd

#print(validate_password())

# i know that syntax errors can't be caught as they the code won't compile, since interpreter won't be happy

def mult_exc():
    a = [1, 2, 3, 4, 0]
    try:
        div = a[8] / a[4]
    except (IndexError, ZeroDivisionError):
        print("index out of range or dividing by 0")

#mult_exc()
