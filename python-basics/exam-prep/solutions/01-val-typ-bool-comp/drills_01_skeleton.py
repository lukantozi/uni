def check_inp_num():
    num = input("Please enter a numeric value: ")
    if num.isnumeric():
        return int(num) * 2
    return "Invalid"
#print(check_inp_num())

def check_between():
    while True:
        try:
            num = int(input("Enter a number between 10 and 20 inclusive: "))
            if 10 <= num <= 20:
                return True 
            else:
                print("\nOut of range. try again...\n")
        except ValueError as e:
            print(f"\n{e}.\nPlease enter only integer values.\n")
#print(check_between())

def difference():
    a = []
    b = []
    print(a == b)
    print(a is b)
#difference()
