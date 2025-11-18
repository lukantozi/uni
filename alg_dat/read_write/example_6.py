import csv

with open("Stars.csv", "r") as file:
    search = input("Enter the data you are searching for: ")
    reader = csv.reader(file)
    for row in reader:
        if search in str(row):
            print(row)
