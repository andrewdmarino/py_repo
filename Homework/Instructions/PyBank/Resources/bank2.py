import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")

total = 0
prev_val=0
row_count = 0
max_val = 0
val_chg = 0
valuelist=[]
max_val= 0
min_val= 0
month_col = []
total_col = []

with open(csvpath) as csvfile:
  my_csv = csv.reader(csvfile, delimiter = ',')
  csv_headings = next(my_csv)
  #first_line = next(my_csv)
  month_col = [0]
  total_col = [1]
  for row in my_csv:
    month_col.append(int(row[1]))
    max_val=max(month_col)
    min_val=min(month_col)
    print(max_val, min_val)
    #print(valuelist)
    current_val = int(row[1])
    prev_val = next(my_csv)[1]  
    #print(current_val)
    #print(prev_val)
    total += int(row[1])
    #print(max_val)
    #row_count + = 1
    #print (row_count)
    #print(first_line[0])
    #print ("\n", total)
csv_output = open(csv_folder / "data_file.txt", 'w')
total_text = f'total is {total} \n'
csv_output.write (total_text)
max_text = f'greatest monthly change is {max_val} \n'
csv_output.write (max_text)
min_text = f'greatest mnonthly loss is {min_val} \n'
csv_output.write (min_text)