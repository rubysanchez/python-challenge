#Import the os module &
#Module for reading CSV files
import os
import csv

#assign variables
total_votes = 0
candidates = []
winning_count = 0
election_winner = ""

#Dictionary for candidate and votes each
candidate_votes = {}


#Set path for the CSV file
csvpath = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')

#Open the CSV file and Read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skips over the headers 
    header = next(csvreader)
    
     
    for row in csvreader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
    
    print("Election Results")
    print("------------------------")
    print("Total Votes: ", total_votes)
    print("------------------------")

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes)/(total_votes)*100

        if (votes > winning_count):
            winning_count = votes
            election_winner = candidate

        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

    print("-------------------------------")
    print("Winner: ", election_winner)


#Export a text file with the results
csvpath_out = os.path.join('.','PyPoll','analysis','Analysis.txt')

with open(csvpath_out, 'w') as Analysis:
    Analysis.write("Election Results")
    Analysis.write("\n")
    Analysis.write("------------------------")
    Analysis.write("\n")
    Analysis.write(f"Total Votes: {str(total_votes)}")
    Analysis.write("\n")
    Analysis.write("------------------------")
    Analysis.write("\n")
    Analysis.write(f"{voter_output}")
    Analysis.write("\n")
    Analysis.write("------------------------")
    Analysis.write("\n")
    Analysis.write(f"Winner: {election_winner}")
