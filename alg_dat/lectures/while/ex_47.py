num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
total = num1 + num2
answer = "y"
num = 0
while answer == "y":
    total = total + num
    answer = input("Would you like to keep adding numbers? [y/n]\n~ ")
    if answer == "y":
        num = int(input("Enter the number to add: "))
    else:
        break
print(f"Total is {total}")
