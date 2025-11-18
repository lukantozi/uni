compnum = 50
count = 0
while True:
    guess = int(input("Try to guess the number: "))
    count = count + 1
    if guess > 50:
        print("Too high")
        continue
    elif guess < 50:
        print("Too low")
        continue
    else:
        print(f"Well done, you took {count} attempts")
        break

