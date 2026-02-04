while True:
    num = int(input("Enter a number between 10 and 20: "))
    if num < 10:
        print("Too low")
        continue
    elif num > 20:
        print("Too high")
    else:
        print("Thank you")
        break
