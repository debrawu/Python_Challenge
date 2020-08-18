import os
import csv

PBcsv = os.path.join("Resources","budget_data.csv")

# print(PBcsv)

#define variables
Months = 0
TotalPL = 0
currentPL = 0
nextPL = 0


#make lists
MonthsList = []
TotalProfitLoss = []


with open(PBcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    #make sure data does not read the header row bc there's no data there
    csvheader = next(csvfile)

    #print out the header
    # print(f"Header: {csvheader}")

    #create loop to read through the data
    for row in csvreader:

#data to find:

#set our values with the corresponding rows
        Months += 1
        TotalPL += int(row[1])
        currentPL = int(row[1])


    #since we'll need the date for the last part of the practice too, append the row to the date
        MonthsList.append(row[0])

#find net total amount of profit/loss in the entire period

    #first set the data to start in row 1 and subtract from current PL - next PL
        currentPL = int(row[1])-nextPL
        TotalProfitLoss.append(currentPL)
        TotalPL = int(row[1])

#total number of months in data set

        Months += 1

#average change of profit/loss in the entire period
    
        average = sum(TotalProfitLoss)/len(TotalProfitLoss)

#net total amount / number of months 
    
        TotalPL = TotalPL + int(row[1])

#greatest increase in profits (date & amount) over entire period

greatest_increase = max(TotalProfitLoss)
increase_index = TotalProfitLoss.index(greatest_increase)
increase_date = MonthsList[increase_index]


#greatest decrease in losses (date & amount) over entire period

greatest_decrease = min(TotalProfitLoss)
decrease_index = TotalProfitLoss.index(greatest_decrease)
decrease_date = MonthsList[decrease_index]

#print data
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {str(Months)}")
print(f"Total: ${str(TotalPL)}")
print(f"Average Change: ${str(average)}")
print(f"Greatest Increase in Profits: {increase_date}")
print(f"Greatest Decrease in Profits: {decrease_date}")