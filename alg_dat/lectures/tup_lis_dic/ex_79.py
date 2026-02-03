nums = []
for _ in range(3):
    while True:
        try:
            nums.append(int(input("Enter a number: ")))
            break
        except ValueError:
            print("Please enter a number")

while True:
    last_number = input("Would you like the last number to remain? [y/n]\n~ ").lower()
    if last_number in ["yes", "y"]:
        break
    elif last_number in ["no", "n"]:
        nums.pop(2)
        break
    else:
        print("Please answer with [yes/y] or [no/n]")

print(nums)

