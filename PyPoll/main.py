#import data 
import os
import csv

#combine files
PyPollData = os.path.join("Resources","election_data.csv")

#print(PyPollData)

#define some variables!
count_votes = 0
TotalVotes = []
AllCandidates = []

with open(PyPollData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #make sure data skips first row!
    next(csvreader)
    
    #start the for loop
    for row in csvreader:

        #set the columns to the correct list - votes = integer value of row 0, candidate = row 2
        count_votes += 1
        Potential_Candidates = row[2]
        count_votes = len(TotalVotes)
   
        #start a loop to find the different candidates and their voter count
        if Potential_Candidates in AllCandidates:
            candidate_index = AllCandidates.index(Potential_Candidates)
            TotalVotes[candidate_index] = TotalVotes[candidate_index] + 1

        else:
            AllCandidates.append(Potential_Candidates)
            TotalVotes.append(1)
    

        print(f'Total Votes: {count_votes}')

# #find percentages
# percentages = []
# most_votes = TotalVotes[0]
# most_votes_index = 0

# #create loop for percentages for each candidate
# for i in range(len(AllCandidates)):
#     voter_percentage = round((TotalVotes[i]/count_votes)*100)
#     percentages.append(voter_percentage)

#     if TotalVotes[i] > most_votes:
#         most_votes = TotalVotes[i]
#         most_votes_index = i

# winner = AllCandidates[most_votes_index]

# # #results
# Election_Results = (f'Election Results\n'
#                     f'---------------------\n'
#                     f'Total Votes: int(count_votes)\n'
#                     f'---------------------\n'
#                     for i in range(len(AllCandidates)):
#                         f'{AllCandidates[i]}: {percentages[i]}.000% ({TotalVotes[i]})\n'
#                     f'---------------------\n'
#                     f'Winner: {str(winner)}\n'
#                     f'---------------------')

# print("Election Results")
# print("--------------------")
# print("Total Votes: (count_votes)")
# print("--------------------")
# for i in range (len(AllCandidates)):
#     print(f"{AllCandidates[i]}: {percentages[i]}.000% ({TotalVotes[i]})")
# print("--------------------")
# print(f"Winner: {str(winner)}")
# print("--------------------")
