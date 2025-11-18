invite = "y"
count = 0
while invite == "y":
    name = input("Enter the name of the person you would like to invite: ")
    count = count + 1
    invite = input("Would you like to invite someone else? [y/any other character for no]\n~ ")
if count == 1:
    print(f"There is {count} people coming to this party")
elif count > 1: 
    print(f"There are {count} people coming to this party")
