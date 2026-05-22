def name_age():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    print(f"Hello {name.upper()}, you are {age} years old")
#name_age()

def num_to_bin():
    num = int(input("Please enter a number: "))
    print("{}".format(bin(num)))
    print(f"{bin(num)}")
#num_to_bin()

def dashes():
    for i in range(1, 5):
        print(i, end="-")
    print(5)
dashes()
