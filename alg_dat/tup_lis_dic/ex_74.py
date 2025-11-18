colors = ["green", "blue", "red", "orange", "yellow", "white", "black", "purple", "grey", "cyan"]

while True:
    try:
        num_1 = int(input("Enter a number between 0 and 4: "))
        if num_1 > 4 or num_1 < 0:
            continue
        break
    except ValueError:
        print("Please enter a number")


while True:
    try:
        num_2 = int(input("Enter a number between 5 and 9: "))
        if num_2 > 9 or num_2 < 5:
            continue
        break
    except ValueError:
        print("Please enter a number")

print(colors[num_1:num_2+1])
