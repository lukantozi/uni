import csv


def choice():
    print()
    print("1) Add to file\n2) View all records\n3) Quit program\n")
    flag = True
    selection = 0
    while flag == True:
        try:
            selection = int(input("Enter the number of your selection: "))
            flag = False
        except ValueError:
            print("Please choose a number between 1 and 3\n")
    return selection


def main():
    flag = True
    while flag == True:
        ch = choice()
        if ch == 1:
            name = input("Enter the name: ")
            salary = input("Enter the salary: ")
            with open("Salaries.csv", "a") as file:
                filewriter = csv.writer(file)
                filewriter.writerow([name, salary])
        elif ch == 2:
            with open("Salaries.csv") as file:
                filereader = csv.reader(file)
                print("Name - Salary")
                for row in filereader:
                    print(' - '.join(row))
        else:
            flag = False

main()
