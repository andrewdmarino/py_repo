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
    prev_val = 0
    loop = 0
    chg_list = []

    for row in my_csv:
        loop +=1
        date = row [0]
        profit = row [1]
       # print(date, profit)
        date_list.append(date)
        profit_list.append(int(row[1]))
       
        if loop>1:
            monthly_chg_val = int(row[1]) - prev_val
            #
            chg_list.append(monthly_chg_val)
            
        prev_val = int(row[1])
    #print(chg_list)    
    num_months=len(date_list)
    total_profit = sum(profit_list)    
    max_profit=max(chg_list)
    min_profit=min(chg_list)
    average_change=round(sum(chg_list)/(len(chg_list)), 2)
    #print(average_change)
    #print(max_profit)
    #print(max_loss)
    #print(total_profit)
    
  
csv_output = open(csv_folder / "data_file.txt", 'w')
months_text = f'number of months is {num_months} \n'
csv_output.write (months_text)
total_text = f'total is {total_profit} \n'
csv_output.write (total_text)
max_text = f'greatest monthly profit is {max_profit} \n'
csv_output.write (max_text)
min_text = f'greatest mnonthly loss is {min_profit} \n'
csv_output.write (min_text)
avg_text= f'the average monthly change is {average_change} \n'     
csv_output.write (avg_text)

print(months_text)
print(total_text)
print(max_text)
print(min_text)
print(avg_text)