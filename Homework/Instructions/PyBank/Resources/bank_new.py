import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyBank/Resources/")
csvpath = Path( csv_folder / "budget_data.csv")

with open(csvpath) as csvfile:
    my_csv = csv.reader(csvfile, delimiter = ',')
    date_list = []
    profit_list = []
    max_profit = 0
    min_profit= 0
    total_profit = 0
    csv_header = next(my_csv)
    
    for row in my_csv:
        date = row [0]
        profit = row [1]
       # print(date, profit)
        date_list.append(date)
        profit_list.append(int(row[1]))
        max_profit=max(profit_list)
        max_loss=min(profit_list)
        total_profit = sum(profit_list)
        for col in my_csv:
            current_val = int(row[1])
            next_check = next(my_csv)#nope
            next_val = int(row[1])
            print(current_val, next_val) #not working
            #val_diff=int(current_val-next_val)
            #print("hello")

    print(max_profit)
    print(max_loss)
    print(total_profit)
        
csv_output = open(csv_folder / "data_file.txt", 'w')
total_text = f'total is {total_profit} \n'
csv_output.write (total_text)
max_text = f'greatest monthly profit is {max_profit} \n'
csv_output.write (max_text)
min_text = f'greatest mnonthly loss is {max_loss} \n'
csv_output.write (min_text)     
    