def division_check():
    flag = True
    main_flag = True
    division = None
    num_1 = 0
    num_2 = 0
    
    while main_flag:
        while flag:
            try:
                num_1 = int(input("Enter the first number: "))
                flag = False
            except ValueError:
                print("Please enter only digits")

        flag = True
        while flag:
            try:
                num_2 = int(input("Enter the second number: "))
                flag = False
            except ValueError:
                print("Please enter only digits")

            try:
                division = num_1 / num_2
                main_flag = False
            except ZeroDivisionError:
                print("Can't devide by 0")

    print(f"Result: {division}")
#division_check()

def password_check():
    flag = True
    while flag:
        try:
            passwd = input("Enter your password: ")
            size = len(passwd)
            if size < 8:
                raise ValueError("Password should be at least 8 characters")
            elif size > 12:
                raise ValueError("Password should be maximum 12 characters")

            upper = False
            for char in passwd:
                if char.isupper():
                    upper = True
                    break

            if not upper:
                raise ValueError("Password must contain at least one upper character")
            flag = False

        except ValueError as e:
            print(e)
#password_check()

def num_check():
    flag = True
    num_1 = 0
    num_2 = 0
    while flag:
        try:
            num_1 = input("Enter the first numeric number: ")
            if not num_1.isnumeric():
                raise TypeError("Only numeric values allowed")
        except TypeError as e:
            print(e)
        else:
            flag = False

    flag = True
    while flag:
        try:
            num_2 = input("Enter the second numeric number: ")
            if not num_2.isnumeric():
                raise TypeError("Only numeric values allowed")
        except TypeError as e:
            print(e)
        else:
            flag = False

    print(f"{num_1}, {num_2}")
#num_check()

def syntax_check():
    a = 5
    try:
        if a > 2: # does not work; the code won't be interpreted
            pass
    except SyntaxError:
        print("You forgot how to write")
#syntax_check()

def fix_code():
    a = 0
    b = 0
    c = None
    flag = True
    while flag:
        try:
            a = int(input("Enter value of a: "))
            flag = False
        except ValueError:
            print("Only digits allowed")

    flag = True
    while flag:
        try:
            b = int(input("Enter value of b: "))
            flag = False
        except ValueError:
            print("Only digits allowed")

    flag = True
    while flag:
        try:
            c = a / b
            flag = False
        except ZeroDivisionError:
            print("Can't divide by 0")
    print("The answer of a divide by b: ", c)
#fix_code()

def get_element(data, index):
    try:
        return data[index]
    except TypeError:
        return None

numbers = [1, 2, 3]
#print(get_element(numbers, "1"))
