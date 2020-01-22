"""Generates a .csv file with a variety of data for the M3 project."""

import csv
from random import randint, uniform, shuffle


# Create lists. "dataset" will contain more lists inside
headers = ["Gender", "Age", "Income", "Education"]
dataset = []
low_skew = []
high_skew = []


# Generate low skew
for x in range(0, 175):
    low_skew.append(round(uniform(3000.01, 58500.99), 2))
for x in range(0, 75):
    low_skew.append(round(uniform(58500.99, 120000.99), 2))
# Generate high skew
for x in range(0, 75):
    high_skew.append(randint(1, 2))
for x in range(0, 175):
    high_skew.append(randint(3, 4))

shuffle(low_skew)
shuffle(high_skew)


# XXX: x in range(0, x) = # of rows
for x in range(0, 250):

    # Create list for each row
    row = []

    # XXX: Generate and append data to row
    row.append(randint(0, 1))  # Column 0
    row.append(randint(18, 80))  # Column 1
    row.append(low_skew[x])  # Column 2
    row.append(high_skew[x])  # Column 3

    # Add row to dataset
    dataset.append(row)


# Open/create dataset.csv
with open('dataset.csv', 'wt') as f:
    # Define csv_writer
    csv_writer = csv.writer(f)

    # Write headers
    csv_writer.writerow(headers)

    # Write dataset
    csv_writer.writerows(dataset)


def lint_check():
    """Simply hides the linter warning, does nothing."""
    None
