# Load dependencies
import os
import csv
import collections
from collections import Counter

# Define file path
csvpath = os.path.join("03-PYTHON", "Homework", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Define variables
totalVotes = 0

# Create lists
namesList = []
candidateVotes = []

#Call file
with open(csvpath) as csvfile:
    # Read file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvreader)   

    # Read through each row of data after the header
    for row in csvreader:
        # The total number of votes cast
        # ---------------------------------------------------------------------------
        totalVotes += 1
        # ---------------------------------------------------------------------------
    
        # A complete list of candidates who received votes
        # ---------------------------------------------------------------------------
        namesList.append(row[2])
        candidate = namesList
        # ---------------------------------------------------------------------------

    # Find the name and total number of votes each candidate won
    # ---------------------------------------------------------------------------
    candidateVotes = Counter(namesList)
    for i, j in candidateVotes.items():
        ({'candidateName':i, 'candidateVotes':j})

    #Find winner with most votes
    # ---------------------------------------------------------------------------
    max_value = max(candidateVotes.values())  
    max_keys = [i for i, j in candidateVotes.items() if j == max_value] 
    winner = max_keys
    # ---------------------------------------------------------------------------
        
    #Print out all results in terminal
    # ---------------------------------------------------------------------------
    nl = '\n'
    print(f'Election Results{nl}------------------------------{nl}Total Votes: {totalVotes}{nl}------------------------------')   
    for i, j in candidateVotes.items():
        print(f'{i}: {j/totalVotes *100:.3f}% ({j})')
    print(f'------------------------------{nl}Winner: {winner[0]}{nl}------------------------------')
    # ---------------------------------------------------------------------------

#Create text file in Analysis folder
# ---------------------------------------------------------------------------
output_path = os.path.join("03-PYTHON", "Homework", "python-challenge", "PyPoll", "Analysis", "election_results.txt")
write_file = open(output_path, 'w+')
write_file.write(f'Election Results' + '\n')
write_file.write(f'------------------------------' + '\n')
write_file.write(f'Total Votes: {totalVotes}' + '\n')
write_file.write(f'------------------------------' + '\n')
for i, j in candidateVotes.items():
    write_file.write(f'{i}: {j/totalVotes *100:.3f}% ({j})' + '\n')
write_file.write(f'------------------------------' + '\n')
write_file.write(f'Winner: {winner[0]}' + '\n')
write_file.write(f'------------------------------')
# ---------------------------------------------------------------------------