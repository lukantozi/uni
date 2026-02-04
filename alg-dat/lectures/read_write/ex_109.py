flag = False
select = None

while flag == False:
    try:
        select = int(input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\nMake a selection 1, 2 or 3: "))
        if select >= 1 and select <= 3:
            flag = True
    except ValueError:
        print("Please enter a number to select")

if select == 1:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(f"{subject}\n")
    file.close()
elif select == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
else:
    subject = input("Enter a school subject: ")
    file = open("Subject.txt", "a")
    file.write(f"{subject}\n")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
