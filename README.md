# python_challenge
Python HW week 3

For this week's challenge, we were instructed to create data to read analysis for both a bank data set and an election data set. With the data, we needed to create new folders for each practice, create folders for the resources & analysis, and create files for each python script and push them into our git repo

PyBank

For the PyBank Data, I needed to analyze the financial records of a company through a CSV file. I needed to find the total number of months, the total P/L for the entire period, the average change of the PL, and the greatest increase and decrease over the period. 

After opening the file, skipping the first line of data and setting variables, I was able to calculate the numbers for months and total P/L and current P/L by creating a for loop and adding those values together from the corresponding row. Then, I was  able to calculate the netChange by subtracting the current from the previous, resetting the values, and appending them to a list to use for our calculations. With that list, I could calculate the average P/L by using the sum of the Average Change List and dividing that by the length of the Average Change list. To make this look nicer, I formatted the number as round, and only used (2) decimal places. Finally, to find the values for greatest increase and decrease, I found that by using the max() function, and created an index for that so that I could determine the date for each of the values. 

To print to a text file, it was recommended to me to create a variable for a multi f string line text so that I could just write one variable instead of multiple lines. I was then able to create a text file with a "with open" function, and determine it as a write-able text file and write to the text file. 

Based on the data, it showed that over the course of 86 months, the company acrued a profit of $38,382,578 dollars, but their average change showed that they were typically losing money by $2,315.12 dollars each month. Their greatest decrease is shown in September of 2013 and their greatest increase in February 2012, so it would be helpful to further investigate why during those months there was so much growth and loss.

PyPoll

For this data set, I was given data from a small, rural town that wanted to modernize the vote counting process. There were (4) candidates running, and the voter ID, county and Candidate that the voter selected were in the CSV file. I needed to find the total number of votes, the complete list of candidates, the percentage of votes for each candidate and the actual number of votes for each, and use those numbers to determine the winner.

Similiarly to the PyBank Data, I opened the file, set the path, created variables & lists and made sure to skip over the first row. Then, I created a for loop so that we could read through each row and column and determine what to do with the values. In this for loop, I added the votes and set the candidates to a specific row. Then, I set an if statement, so that if there was a new candidate in the row, they would be added to the index, and their vote would be counted for them. If not, it would continue to add the value for the same candidate.

To calculate percentage, I set new variables and lists and then created a for loop to go through the entire range of All Candidates to calculate the percentage of each candidate's votes and then attached those values to the a voter percentage list. Within that, I put an if statement, to see who had the most votes and that would determine the winner. 

Finally, I printed the results to a txt file - because there is a for loop, I was not able to do the same as the PyBank Data, so I had to create multiple .write lines to write to the txt file.
