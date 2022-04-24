#create file paths across operating systems
import os

# Module for reading CSV files
import csv
csvpath = os.path.join('PyPoll/Resources/election_data.csv')

#Varables
total_votes_obtained = 0
candidate = []
charles_votes = 0
diana_votes = 0
raymon_votes = 0
winner = []

# Look through PyPole File
with open(csvpath, 'r') as PyPollFile:
    csv_reader = csv.reader(PyPollFile, delimiter=",")
    csv_header = next(PyPollFile)

    # look through candidate votes and count the votes for each candidate
    for row in csv_reader:
        total_votes_obtained += 1
        candidate.append(row[2])
        # count Charles Casper Stockham votes
        if row[2] == 'Charles Casper Stockham':
            charles_votes  += 1
        # count Diana DeGette votes
        elif row[2] == 'Diana DeGette':
            diana_votes  += 1
        # count Raymon Anthony Doane votes
        else:
            raymon_votes  += 1
          
# look through Candidate list
def unique(blank):
    unique_list = []     
    for x in blank:
        if x not in unique_list:
            unique_list.append(x)        
    return unique_list
candidates = list(unique(candidate))

# Identify the Candidate that won
if charles_votes  > diana_votes  and charles_votes  > raymon_votes :
        winner = candidates[0]
elif diana_votes  > charles_votes  and diana_votes  > raymon_votes :
        winner = candidates[1]
elif raymon_votes  > charles_votes  and raymon_votes  > diana_votes :
        winner = candidates[2]
else:
    pass

#print out table
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {total_votes_obtained}")
print("--------------------------------")
print(f"Charles Casper Stockham: {'{:.3%}'.format(charles_votes /total_votes_obtained)} ({charles_votes })")
print(f"Diana DeGette: {'{:.3%}'.format(diana_votes /total_votes_obtained)} ({diana_votes })")
print(f"Raymon Anthony Doane: {'{:.3%}'.format(raymon_votes /total_votes_obtained)} ({raymon_votes })")
print("--------------------------------")
print(f"Winner: {winner}")

# Print table onto a text file
csvpath2 = os.path.join('PyPoll/Analysis/PyPoll_Analysis.txt')
with open(csvpath2, "w", newline = "") as text:

    text.write("Election Results\n")
    text.write("--------------------------------\n")
    text.write(f"Total Votes: {total_votes_obtained}\n")
    text.write("--------------------------------\n")
    text.write(f"Charles Casper Stockham: {'{:.3%}'.format(charles_votes /total_votes_obtained)} ({charles_votes })\n")
    text.write(f"Diana DeGette: {'{:.3%}'.format(diana_votes /total_votes_obtained)} ({diana_votes })\n")
    text.write(f"Raymon Anthony Doane: {'{:.3%}'.format(raymon_votes /total_votes_obtained)} ({raymon_votes })\n")
    text.write("--------------------------------\n")
    text.write(f"Winner: {winner}\n")