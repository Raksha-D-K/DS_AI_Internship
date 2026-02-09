import csv

with open("src/Day7/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
