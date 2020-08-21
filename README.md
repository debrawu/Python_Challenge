# python_challenge
Python HW week 3

For this week's challenge, we were instructed to create data to read analysis for both a bank data set and an election data set. With the data, we needed to create new folders for each practice, create folders for the resources & analysis, and create files for each python script and push them into our git repo

#PyBank
For the PyBank Data, I needed to analyze the financial records of a company through a CSV file. I needed to find the total number of months, the total P/L for the entire period, the average change of the PL, and the greatest increase and decrease over the period. 

After opening the file, skipping the first line of data and setting variables, I was able to calculate the numbers for months and total P/L and current P/L by creating a for loop and adding those values together from the corresponding row. Then, I was  able to calculate the netChange by subtracting the current from the previous, resetting the values, and appending them to a list to use for our calculations. With that list, I could calculate the average P/L by using the sum of the Average Change List and dividing that by the length of the Average Change list. To make this look nicer, I formatted the number as round, and only used (2) decimal places. Finally, to find the values for greatest increase and decrease, I found that by using the max() function, and created an index for that so that I could determine the date for each of the values. 

To print to a text file, it was recommended to me to create a variable for a multi f string line text so that I could just write one variable instead of multiple lines. I was then able to create a text file with a "with open" function, and determine it as a write-able text file and write to the text file. 

Based on the data, it showed that over the course of 86 months, the company acrued a profit of $38,382,578 dollars, but their average change showed that they were typically losing money by $2,315.12 dollars each month. Their greatest decrease is shown in September of 2013 and their greatest increase in February 2012, so it would be helpful to further investigate why during those months there was so much growth and loss.


