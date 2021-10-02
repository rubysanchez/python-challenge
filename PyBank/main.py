#Import the os module &
#Module for reading CSV files
import os
import csv
from typing import Counter

#Set path for the CSV file
csvpath = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

#Open the CSV file and Read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips over the headers so it doesn't impact counts
    header = next(csvreader)

    #Loop through each row in the data set and push variables to empty arrays
    #Total_Months is a count of the rows in first column (or index 0)
    #Net_Total_PL is basically the sum of all the data in column 2 (or index 1)
    #Change_PL is the difference from month to month in the profit/loss
    Total_Months = []
    Net_Total_PL = []
    Change_PL = []
    for row in csvreader:
        Total_Months.append(row[0])
        Net_Total_PL.append(int(row[1]))
    for i in range(len(Net_Total_PL)-1):
        Change_PL.append(Net_Total_PL[i+1]-Net_Total_PL[i])

    #find the average of the change in profit/loss
    #Used Round function to 2 digits because this is a dollar amount
    Average_Change_PL = round(sum(Change_PL)/len(Change_PL),2)

    #Identify the greatest increase and decrease in the Change_PL Array
    Greatest_Inc = max(Change_PL)
    Greatest_Dec = min(Change_PL)

    #Now that I have the Greatest_Inc and Greatest_Dec, use index function to find the index of corresponding date 
    #THEN store actual date from within Total_Months Array
    Index_Inc_Date = Change_PL.index(max(Change_PL))+1
    Greatest_Inc_Date = Total_Months[Index_Inc_Date]

    Index_Dec_Date = Change_PL.index(min(Change_PL))+1
    Greatest_Dec_Date = Total_Months[Index_Dec_Date]

#Print out my analysis
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(Total_Months)}")
print(f"Total: ${sum(Net_Total_PL)}")
print(f"Average Change: {Average_Change_PL}")
print(f"Greatest Increase in Profits: {Greatest_Inc_Date} (${Greatest_Inc})")
print(f"Greatest Decrease in Profits: {Greatest_Dec_Date} (${Greatest_Dec})")

#Export a text file with the results
csvpath_out = os.path.join('.','PyBank','analysis','Analysis.txt')

with open(csvpath_out, 'w') as Analysis:
    Analysis.write("Financial Analysis")
    Analysis.write("\n")
    Analysis.write("------------------------")
    Analysis.write("\n")
    Analysis.write(f"Total Months: {len(Total_Months)}")
    Analysis.write("\n")
    Analysis.write(f"Total: ${sum(Net_Total_PL)}")
    Analysis.write("\n")
    Analysis.write(f"Average Change: {Average_Change_PL}")
    Analysis.write("\n")
    Analysis.write(f"Greatest Increase in Profits: {Greatest_Inc_Date} (${Greatest_Inc})")
    Analysis.write("\n")
    Analysis.write(f"Greatest Decrease in Profits: {Greatest_Dec_Date} (${Greatest_Dec})")

