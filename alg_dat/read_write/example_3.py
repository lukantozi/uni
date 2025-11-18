with open("Stars.csv", "a") as file:
    name = input("Enter name: ")
    age = input("Enter age: ")
    star = input("Enter star: ")
    new_record = name + ',' + age + ',' + star + '\n'
    file.write(str(new_record))
