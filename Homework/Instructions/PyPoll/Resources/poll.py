import os
from pathlib import Path
import csv

csv_folder = Path("Homework/Instructions/PyPoll/Resources/")
csvpath = Path( csv_folder / "election_data.csv")

with open(csvpath) as csvfile:
    my_csv = csv.reader(csvfile, delimiter = ',')
    csv_header = next(my_csv)
    voter_id = []
    county = []
    candidate = []
    khan_votes = 0
    corey_votes = 0
    li_votes = 0
    oleary_votes = 0
    loop_ctr = 0
    print(csv_header)

    for row in my_csv:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        #print (candidate) works 
        if (candidate == 'Khan'):
            khan_votes +=1 
            loop_ctr+=1
        #elif (candidate == 'Corey'): 
        #    corey_votes +=1
        #elif (candidate == 'Li'):
        #    li_votes + = 1
        #else:
        #    oleary_votes+ =1
            
    print(khan_votes) #2mill votes?
    #print(corey_votes)
    #print(li_votes)
    #print(oleary_votes)  
    print(loop_ctr)   