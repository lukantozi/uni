import csv

with open("Stars.csv", "r") as file:
    rows = list(csv.reader(file))
    print(rows[1])
