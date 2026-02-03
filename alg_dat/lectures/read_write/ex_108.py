name = input("Please enter a name: ")
file = open("Names.txt", "a")
file.write(f"{name}\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()
