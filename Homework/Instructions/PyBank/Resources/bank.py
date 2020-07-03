import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path(csv_folder / "budget_data.csv")
csv_output = open(csv_folder / "data_file.txt", 'w')

total = 0
prev_val=0
current_val=0
change_value=0

#def monthly_change(monthly_chg_value)>:  try to define a fuction call to calc the change


with open(csvpath) as csvfile:
    for row in csvfile
        first_line= 
    