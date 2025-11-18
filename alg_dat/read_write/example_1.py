file = open("Countries.txt", "a")
file.write("France\n")
file.close()

file = open("Countries.txt", "r")
print(file.read())
file.close()
