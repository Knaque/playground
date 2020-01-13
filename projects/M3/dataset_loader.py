"""Automatically loads dataset into lists."""

import csv


# Create empty lists
gender = []
age = []
income = []
education = []


# Open dataset.csv
with open("dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for lines in csv_reader:
        gender.append(float(lines[0]))
        age.append(float(lines[1]))
        income.append(float(lines[2]))
        education.append(float(lines[3]))


# Sort lists
gender.sort()
age.sort()
income.sort()
education.sort()
