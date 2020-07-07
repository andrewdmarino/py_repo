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
        
        #check matches by candidate name and add vote in loop od candidate list
        if candidate == 'Khan':
            khan_votes +=1 
        elif candidate == 'Correy': 
            correy_votes +=1
        elif candidate == 'Li':
            li_votes +=1
        else:
            oleary_votes +=1

    total_votes = khan_votes+correy_votes+li_votes+oleary_votes
    #output to terminal output
    print("khan votes = ", khan_votes) 
    print("khan won ", ((khan_votes/total_votes)*100), "percentage of votes")
    print("correy votes = ", correy_votes)
    print("correy won ", ((correy_votes/total_votes)*100), "percentage of votes")
    print("li votes = ", li_votes)
    print("li won ", ((li_votes/total_votes)*100), "percentage of votes")
    print("oleary votes = ",oleary_votes)  
    print("O'leary won", ((oleary_votes/total_votes)*100), "percentage of votes")
    print("total votes cast= ", total_votes)


 