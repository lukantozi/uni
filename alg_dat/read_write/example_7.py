import csv


with open("Stars.csv") as file:
    file = list(csv.reader(file))
    tmp = []
    for row in file:
        tmp.append(row)

with open("new_stars.csv", "w") as file:
    x = 0
    for row in tmp:
        new_rec = tmp[x][0] + ',' + tmp[x][1] + ',' + tmp[x][2] + '\n'
        file.write(new_rec)
        x = x + 1
