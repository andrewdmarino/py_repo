import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")

total = 0
prev_val=0
row_count = 0

#month_col = [0]
#total_col = [1]

with open(csvpath) as csvfile:
  my_csv = csv.reader(csvfile, delimiter = ',')
  csv_headings = next(my_csv)
  #first_line = next(my_csv)
  for row in my_csv:
    #print (row_count)
    #print(row)
    #prev_val = int(row[row_count-1]) // this is the column number
    prev_val = (row[1].index)
    print(prev_val)
    current_val = int(row[1])
    total += int(row[1])
    row_count + = 1
    #print (row_count)
#print(first_line[0])
print ("\n", total)
csv_output = open(csv_folder / "data_file.txt", 'w')
total_text = f'total is {total} \n'
csv_output.write (total_text)
