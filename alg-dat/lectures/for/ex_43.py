while True:
    direction = input("Would you like to count up or down?\n~ ").lower()
    if direction == "up":
        top_num = int(input("Enter the top number: "))
        for i in range(1, top_num + 1):
            print(i)
        break
    elif direction == "down":
        below_20 = int(input("Enter the number below 20: "))
        for i in range(20, below_20-1, -1):
            print(i)
        break
    else:
        print("Please choose the direction")
