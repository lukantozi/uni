def name_age():
    name = input("Please enter your name: ").upper()
    age = int(input("Please enter yout age: "))
    print(f"Hello {name}, you are {age:0b} years old")
#name_age()

def sum_of_first_three():
    nums = []
    with open("example1.txt", "r+") as file:
        for _ in range(4):
            line = file.readline()
            nums.extend(line.split())
        sum_nums = sum([int(num) for num in nums]) 
        file.write(str(sum_nums))
        print("{:.2f}".format(sum_nums))
#sum_of_first_three()

def how_many_lines():
    with open("example1.txt", "r") as file:
        lines = len(file.readlines())
        print(lines)
    with open("example1.txt", "r") as file:
        first_three = file.read(4)
        print(first_three)
    with open("example2.txt", "w") as file:
        file.write(str(lines))
        file.write(first_three)
#how_many_lines()

def strip_newline():
    stripped = []
    with open("example1.txt", "r") as file:
        lines = file.readlines()
    stripped = [line.strip("\n") for line in lines]
    print(stripped)
    with open("example1_stripped.txt", "w") as file:
        file.write("".join(stripped))
#strip_newline()

import string 

def alphabet_in_lines(n):
    letters = list(string.ascii_uppercase)
    with open(f"letters_by_{n}.txt", "a") as file:
        iterations = 26 // n
        ptr = 0
        for _ in range(iterations):
            file.write(f"{"".join((letters[ptr:ptr+n]))}\n")
            ptr += n
        file.write(f"{"".join((letters[ptr:]))}")
#alphabet_in_lines(4)
#alphabet_in_lines(13)

def two_files():
    with open("example1.txt") as file1, open("letters_by_4.txt") as file2:
        for num, lines in enumerate(zip(file1, file2)):
            print(f"line {num+1} from file 1: {lines[0].strip().ljust(8)} - line {num+1} from file 2: {lines[1].strip()}")
#two_files()
