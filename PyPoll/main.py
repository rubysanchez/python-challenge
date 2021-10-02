#Import the os module &
#Module for reading CSV files
import os
import csv

#Set path for the CSV file
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

#Open the CSV file and Read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips over the headers so it doesn't impact counts
    header = next(csvreader)

    #Loop through each row in the data set and push variables to empty arrays
    #Total_Votes is a count of the rows in first column (or index 0)
    #Candidates is where I'll store a list of each unique candidate in file from column 3 or index 2
    Total_Votes = []
    Candidates = []
    for row in csvreader:
        Total_Votes.append(row[0])
        Candidate = row[2]

        #Determine votes per candidate
        #Candidate respresents individual candidate. Candidates is the Array.
        #Each time a candidate appears, add 1 to the count
        if Candidate in Candidates:
            candidate_index = Candidates.index(Candidate)
            Total_Votes[candidate_index] = Total_Votes[candidate_index] + 1
        else:
            Candidates.append(Candidate)
            Total_Votes.append(1)

    #Calculate the Percentage of votes