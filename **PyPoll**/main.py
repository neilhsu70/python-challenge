# call dependencies
import os
import csv

# Path to collect data from the Resources folder
py_poll = os.path.join("Resources","election_data.csv")

# Assign Variables
total_votes = 0
candidate_dict = {}
candidate = ""
winner_votes = 0
winner = ""

with open(py_poll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

# Calculates total votes, using a dictionary to append names, counts votes for each candidate
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidate_dict:
            candidate_dict.update([(row[2], 0)])
        if row[2] in candidate_dict:
            candidate = row[2]
            candidate_dict[candidate] = candidate_dict[candidate] + 1
            
# Calculates Number of Candidates
number_candidates = len(candidate_dict)

# Print results in Terminal
print("Election Results by Neil Hsu")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for row in range(number_candidates):
    print(f"{list(candidate_dict.keys())[row]}: {int((candidate_dict[list(candidate_dict.keys())[row]] / total_votes) * 100)}% ({(candidate_dict[list(candidate_dict.keys())[row]])})")

print("-------------------------")
for row in range(number_candidates):
    if int(candidate_dict[list(candidate_dict.keys())[row]]) > winner_votes:
        winner_votes = int(candidate_dict[list(candidate_dict.keys())[row]])
        winner = list(candidate_dict.keys())[row]

print(f"Winner: {winner}")    
print("-------------------------")

# Export to .txt file
with open("ElectionResults.txt", "w") as text_file:
    print("Election Results by Neil Hsu", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("-------------------------", file=text_file)
    for row in range(number_candidates):
        print(f"{list(candidate_dict.keys())[row]}: {int((candidate_dict[list(candidate_dict.keys())[row]] / total_votes) * 100)}% ({(candidate_dict[list(candidate_dict.keys())[row]])})", file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)    
    print("-------------------------", file=text_file)