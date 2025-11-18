file = open("Countries.txt", "w")
file.write("Italy\n")
file.write("Germany\n")
file.write("Spain\n")
file.close()

file = open("Countries.txt", "r")
print(file.read())
file.close()

