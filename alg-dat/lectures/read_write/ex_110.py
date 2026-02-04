with open("Names.txt", "r") as file:
    names = file.read()
    print(names)

name = input("Enter one of the names above: ")
with open("Names_1.txt", "w") as file:
    new_names = names.replace(name+"\n", '')
    file.write(new_names)

with open("Names_1.txt", "r") as file:
    text = file.read()
    print(text)
