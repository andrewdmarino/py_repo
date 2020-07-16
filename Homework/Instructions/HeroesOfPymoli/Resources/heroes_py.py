import pandas as pd
import numpy as np 
import os
from pathlib import Path
import csv

data_folder = Path("Pandas/Instructions/HeroesOfPymoli/Resources")
data_path = Path( data_folder / "purchase_data.csv")

print (data_path)
# File to Load 
my_df = pd.read_csv(data_path)
my_df



# Read Purchasing File and store into Pandas data frame
#purchase_data = pd.DataFrame(my_df)


# Display the total number of players
# Purchasing Analysis (Total)
#  Run basic calculations to obtain number of unique items, average price, etc.

 
#  Create a summary data frame to hold the results


# Optional: give the displayed data cleaner formatting


# Display the summary data frame


# Gender Demographics

# * Percentage and Count of Male Players

# * Percentage and Count of Female Players

# * Percentage and Count of Other / Non-Disclosed

#  Purchasing Analysis (Gender)
#  Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
 
 
  
# * Create a summary data frame to hold the results
 
 
# * Optional: give the displayed data cleaner formatting

 
# * Display the summary data frame

#  Age Demographics

# * Establish bins for ages

# * Categorize the existing players using the age bins. Hint: use pd.cut()

# * Calculate the numbers and percentages by age group

# * Create a summary data frame to hold the results

# * Optional: round the percentage column to two decimal points

# * Display Age Demographics Table


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age


# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below


# * Create a summary data frame to hold the results
 
 
# * Optional: give the displayed data cleaner formatting

 
# * Display the summary data frame

#  Top Spenders

# * Run basic calculations to obtain the results in the table below


# * Create a summary data frame to hold the results

 
# * Sort the total purchase value column in descending order


# * Optional: give the displayed data cleaner formatting


# * Display a preview of the summary data frame

 
#  Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
 
# 
# * Sort the purchase count column in descending order


# * Optional: give the displayed data cleaner formatting


# * Display a preview of the summary data frame


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order

# 
# * Optional: give the displayed data cleaner formatting

# 
# * Display a preview of the data frame
