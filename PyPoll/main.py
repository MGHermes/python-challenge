"""
In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be given a set of poll data called [election_data.csv] (PyPoll/Resources/election_data.csv).
The dataset is composed of three columns: "Voter ID", "County", and "Candidate".
Your task is to create a Python script that analyzes the votes and calculates each of the following:
    * The total number of votes cast
    * A complete list of candidates who received votes
    * The percentage of votes each candidate won
    * The total number of votes each candidate won
    * The winner of the election based on popular vote.

Your analysis should look similar to the following:
  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```
"""

import os #allows for us to use file pathing
import csv #allows for us to handle csv files

# Store the file path associated with the file
election_data_csv = os.path.join("Resources","election_data.csv")

# Create the necessary variables
candidateList = []
totalVotes = 0
charlesTotal = 0
charlesPercent = 0
dianaTotal = 0
dianaPercent = 0
raymonTotal = 0
raymonPercent = 0
winner = ""

# Open the file and read it using the budget_data_csv file path
with open(election_data_csv) as csvfile:

    # Use csv.reader() function to open the file
    csvReader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    header = next(csvReader)

    # Go through the rows in the csvReader
    for row in csvReader:
        
        # Add candidate to candidatesList if necessary
        if row[2] not in candidateList:
            candidateList.append(row[2])

        # Add one to the total votes
        totalVotes += 1

        # If Charles, add to the Charles Total
        if row[2] == "Charles Casper Stockham":
            charlesTotal += 1

        # If Diana, add to the Diana Total
        if row[2] == "Diana DeGette":
            dianaTotal += 1
        
        # If Raymon, add to the Raymon Total
        if row[2] == "Raymon Anthony Doane":
            raymonTotal += 1

charlesPercent = (charlesTotal/totalVotes)*100
dianaPercent = (dianaTotal/totalVotes)*100
raymonPercent = (raymonTotal/totalVotes)*100

if charlesPercent >= 50:
    winner = "Charles Casper Stockham"
elif dianaPercent >= 50:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
print(f"Charles Casper Stockham: {charlesPercent:.3f}% ({charlesTotal})")
print(f"Diana DeGette: {dianaPercent:.3f}% ({dianaTotal})")
print(f"Raymon Anthony Doane: {raymonPercent:.3f}% ({raymonTotal})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")