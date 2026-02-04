import random

def main():
    score = 0
    for n in range(5):
        num_1 = random.randint(0, 100)
        num_2 = random.randint(0, 100)
        answer = validate_integer(num_1, num_2, n)
        if answer == num_1 + num_2:
            score += 1
    print(f"\nYour final score: [{score}/5] --> {score/5*100}%")

def validate_integer(num_1, num_2, n):
    while True:
        try:
            num = int(input(f"\nQuestion {n+1}:\n{num_1} + {num_2} = "))
            return num
        except ValueError:
            print("Please enter the integer\n")
                

if "__main__" == __name__:
    main()
