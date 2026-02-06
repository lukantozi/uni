from math import sqrt, log
import math, random, statistics
import datetime

def circle_area():

    pi = math.pi
    r = int(input("Enter the radius in cm: "))
    area = round(pi * r**2, 2)
    return area

#print(f"area of the circle: {circle_area()} cm^2")

def root():

    flag = True
    num = 0
    while flag:
        try:
            num = int(input("Enter a number to take a square out of: "))
            if num >= 0:
                flag = False
            else:
                print("The number should be more than equal to 0")
        except ValueError:
            print("Please enter only numbers")


    return round(sqrt(num), 2), round(log(num), 2)

#r, l = root()
#print(f"square root: {r}\nnatural logarithm: {l}")

def ran_stat():
    random.seed(5)

    nums = [random.randint(1, 100) for _ in range(10)]

    avg = sum(nums) / len(nums)  
    nums_min = min(nums)
    nums_max = max(nums)
    nums_stdev = statistics.stdev(nums)

    return f"average: {avg}\nminimum: {nums_min}\nmaximum: {nums_max}\nstandard deviation: {round(nums_stdev, 2)}\n"

#print(ran_stat())

def guess_the_num():
    flag = True
    guesses = 0
    num = random.randint(1, 50)

    while flag:
        try:
            guess = int(input("Guess the number: "))
            guesses += 1
            if guess > num:
                print("Too high. Try again...")
            elif guess < num:
                print("Too low. Try again...")
            else:
                print(f"You've guessed correctly, and took you {guesses} tries")
                flag = False
        except ValueError:
            print("Enter only numbers")

#guess_the_num()

def day_time():
    now = datetime.datetime.now()
    date = now.strftime("%x")
    time = now.strftime("%X")
    weekday = now.strftime("%A")
    print(date, time, weekday)
#day_time()

def convert_birthday():
    birth = input("Enter your birthday [YYYY-MM-DD]: ")
    year, month, day = birth.split("-")

    now = datetime.datetime.now()

    dif = now - datetime.datetime(int(year), int(month), int(day))

    days = dif.days

    print(days)
    print(days // 365)

#convert_birthday()
