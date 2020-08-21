import os
import csv

PBcsv = os.path.join("Resources","budget_data.csv")

# print(PBcsv)

#define variables
Months = 1
TotalPL = 0
currentPL = 0
nextPL = 0

netChange = 0

#make lists
MonthsList = []
TotalProfitLoss = []
AverageChange = []


with open(PBcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    #make sure data does not read the header row bc there's no data there
    csvheader = next(csvreader)
    first = next(csvreader)
    previousPL = int(first[1])

    #print out the header
    # print(f"Header: {csvheader}")

    #create loop to read through the data
    for row in csvreader:

#data to find:

#set our values with the corresponding rows
        Months += 1
        TotalPL += int(row[1])
        currentPL = int(row[1])
        
        #net change= current PL - previous PL
        netChange = currentPL - previousPL
        AverageChange.append(netChange)
        
        #how to make current pl to previous pl and store the values
        #set previousPL to currentPL
        previousPL = currentPL

    #since we'll need the date for the last part of the practice too, append the row to the date
        MonthsList.append(row[0])

#find net total amount of profit/loss in the entire period

    #first set the data to start in row 1 and subtract from current PL - next PL
        currentPL = int(row[1])-nextPL
        TotalProfitLoss.append(currentPL)
        # TotalPL = int(row[1])

#total number of months in data set

        # Months += 1

#average change of profit/loss in the entire period
    
average = round(sum(AverageChange)/len(AverageChange),2)

#net total amount / number of months 
    
        # TotalPL = TotalPL + int(row[1])

#greatest increase in profits (date & amount) over entire period

greatest_increase = max(TotalProfitLoss)
increase_index = TotalProfitLoss.index(greatest_increase)
increase_date = MonthsList[increase_index]


#greatest decrease in losses (date & amount) over entire period

greatest_decrease = min(TotalProfitLoss)
decrease_index = TotalProfitLoss.index(greatest_decrease)
decrease_date = MonthsList[decrease_index]

#print data
#put a variable = list of f string, and then set (1) print and it will print the entire variable

Financial_Analysis = (f'Financial Analysis:\n'
                      f'--------------------\n'
                      f'Total Months: {str(Months)}\n'
                      f'Total: ${TotalPL}\n'
                      f'Average Change: ${average}\n'
                      f'Greatest Increase in Profits: {increase_date} \t${greatest_increase}\n'
                      f'Greatest Decrease in Profits: {decrease_date} \t${greatest_decrease}')

print(Financial_Analysis)

# print(f"Financial Analysis")
# print(f"----------------------------")
# print(f"Total Months: {str(Months)}")
# print(f"Total: ${str(TotalPL)}")
# print(f"Average Change: ${str(average)}")
# print(f"Greatest Increase in Profits: {increase_date}")
# print(f"Greatest Decrease in Profits: {decrease_date}")

#export to a txt file with a with open & 'w', use the same variable from the print function 
with open("Financial_Analysis.txt","w") as f:
        f.write(Financial_Analysis)
