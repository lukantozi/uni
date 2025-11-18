num_of_people = int(input("How many people would you like to invite?\n~ ")) 
if num_of_people < 10:
    for _ in range(num_of_people):
        name = input("Please enter the guest's name: ")
        print(f"{name} has been invited.")
else:
    print("Too many people")
