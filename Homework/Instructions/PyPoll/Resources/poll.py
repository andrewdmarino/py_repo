import os
from pathlib import Path
import csv
import math

csv_folder = Path("Homework/Instructions/PyPoll/Resources/")
csvpath = Path( csv_folder / "election_data.csv")

with open(csvpath) as csvfile:
    my_csv = csv.reader(csvfile, delimiter = ',')
    csv_header = next(my_csv)
    voter_id = []
    county = []
    candidate = []
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    oleary_votes = 0
    total_votes = 0    

    print(csv_header)

    for row in my_csv:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        
        #check matches by candidate name and add vote in loop of candidate list
        if candidate == 'Khan':
            khan_votes +=1 
        elif candidate == 'Correy': 
            correy_votes +=1
        elif candidate == 'Li':
            li_votes +=1
        else:
            oleary_votes +=1

    total_votes = khan_votes+correy_votes+li_votes+oleary_votes
    #output to terminal output / round to nearest % 
    print("khan votes = ", khan_votes) 
    print("khan recieved ", ((khan_votes/total_votes)*100), "percentage of votes")
    print("correy votes = ", correy_votes)
    print("correy recieved ", ((correy_votes/total_votes)*100), "percentage of votes")
    print("li votes = ", li_votes)
    print("li recieved ", ((li_votes/total_votes)*100), "percentage of votes")
    print("O'leary recieved", ((oleary_votes/total_votes)*100), "percentage of votes")
    print("total votes cast= ", total_votes)

    khan_percent = (round((khan_votes/total_votes)*100, 2)) 
    correy_percent =(round((correy_votes/total_votes)*100, 2))
    li_percent = (round((li_votes/total_votes)*100, 2))
    oleary_percent = (round((oleary_votes/total_votes)*100, 2))
    

csv_output = open(csv_folder / "data_file.txt", 'w')

total_text = f'total votes cast {total_votes} \n'
spacer_text =f'--------------------\n'
csv_output.write(spacer_text)
csv_output.write (total_text)
csv_output.write(spacer_text)
khan_text = f'Khan received {khan_percent} percent of the vote \n'
csv_output.write(khan_text)
correy_text = f'Correy received {correy_percent} percent of the vote \n'
csv_output.write (correy_text)
li_text = f'Li received {li_percent} percent of the vote \n'
csv_output.write(li_text)
oleary_text = f'Oleary received {oleary_percent} percent of the vote \n'
csv_output.write(oleary_text)
csv_output.write(spacer_text)
winner_text = f'and the winner of the election with {khan_votes} votes is Khan with {khan_percent} percent of the total votes \n'
csv_output.write (winner_text)

#should just print the text vars to terminal here