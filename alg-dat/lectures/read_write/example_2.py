import csv

with open("Stars.csv", "w") as file:
    new_record = "Brian,73,Taurus\n"
    file.write(str(new_record))
