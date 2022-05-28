# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path

file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Add the total vote counter and set to zero

total_votes = 0

# Candidate options

candidate_options = []

# Declare empty dictionary - Candidate Votes

candidate_votes = {}

# Winning Candidate and Winning Count Tracker Variables

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:

        # Increment the total votes by 1 (initialize a variable called an accumulator)
        total_votes += 1

        # Print candidate name for each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin trackign that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

# Determine the percentage of votes for each candidate by looping thourgh the counts
# 1. Iterate trhough the candidate list
for candidate_name in candidate_votes:

    # 2. Retrieve the vote count of a candidate
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100



    #Determine the winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # And, set the winning_candidate equal to the candidates name
        winning_candidate = candidate_name
    
    # To Do: print out each of the candiate's name, vote count
    # and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"winning Percentage: {winning_percentage: .1f}%\n"
    f"-----------------------\n")

print(winning_candidate_summary)
