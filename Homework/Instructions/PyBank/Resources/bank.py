import os
from pathlib import Path
import csv
csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")


print(csvpath)

# read csv

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    row_count = sum(1 for row in csvreader)
    print (row_count)
    
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
   # for row in csvreader:
    #    print(row)