"""Automatically loads dataset into lists."""

import csv


# Create empty lists
gender_raw = []
age_raw = []
income_raw = []
education_raw = []


# Open dataset.csv
with open("dataset.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for lines in csv_reader:
        gender_raw.append(float(lines[0]))
        age_raw.append(float(lines[1]))
        income_raw.append(float(lines[2]))
        education_raw.append(float(lines[3]))


# Sort lists
gender = sorted(gender_raw)
age = sorted(age_raw)
income = sorted(income_raw)
education = sorted(education_raw)
