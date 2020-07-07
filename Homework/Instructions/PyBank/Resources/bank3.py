import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")

row_count = 0 #num rows in the month col
current_val = 0 #assign current value of total col
next_val =  0 #assign val of next row of total col
max_val= 0 #get highest val in total col
min_val= 0 #assign lowest vol in total col
month_col = [] #list of all month rows val
total_col = [] #list of all total rows val
total = 0 # add all the vals from the total col list as int
diff_val=[] # 

with open(csvpath) as csvfile:
  my_csv = csv.reader(csvfile, delimiter = ',')
  csv_headings = next(my_csv)
  #first_line = next(my_csv)
  month_col = [0]
  total_col = [1]

  for row in my_csv:
    total_col.append(int(row[1]))
    max_val=max(total_col)
    min_val=min(total_col)
    
    month_count = (month_col.count)
    
    current_val = int(row[1])
    #next_val = next(row[1])
    
    total=sum(total_col)
    #diff_val = (current_val-next_val)
    #print(current_val, next_val)
   
    #total+= total_col
    #end loop actions
csv_output = open(csv_folder / "data_file.txt", 'w')
total_text = f'total is {total} \n'
csv_output.write (total_text)
max_text = f'greatest monthly profit is {max_val} \n'
csv_output.write (max_text)
min_text = f'greatest mnonthly loss is {min_val} \n'
csv_output.write (min_text)