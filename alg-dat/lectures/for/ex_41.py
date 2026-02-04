name = input("Enter your name: ")
num = int(input("Enter a number: "))
while True:
    if num < 10:
        for _ in range(num):
            print(name)
        break
    else:
        print("Too high")
        num = int(input("Enter a number: "))
