import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")
csv_output = open(csv_folder / "data_file.txt", 'w')
total = 0
prev_val=0
current_val=0
#def monthly_change(monthly_chg_value)>:  try to define a fuction call to calc the change
with open(csvpath) as csvfile:
    #csvreader object loads csfile (budget_data.csv) and explicitly adds ',' delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #skip header
    
    for row in csvreader:
        #prev_val = (int(row[-1])
        current_val = (int(row[1])    
        #print (prev_val-monthly_val)
        total+ =int(row[1])     

print(total)