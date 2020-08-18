#import data 
import os
import csv

#combine files
PyPollData = os.path.join("Resources","election_data.csv")

#print(PyPollData)

#define some variables!
votes = 0
count_votes = []
candidates  = []

with open(PyPollData) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #make sure data skips first row!
    next(csvreader)
    
    #start the for loop
    for row in csvreader

    
