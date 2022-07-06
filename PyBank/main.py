"""
You will be given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following:
    * The total number of months included in the dataset
        count up the number of months, looping through the file
    * The net total amount of "Profit/Losses" over the entire period
    * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        create a new list:
            1st value is first value in the budget list
            2nd value is the 2nd value minus the 1st value
            3rd value is the 4th value minus the 2nd value and so forth
        should have one less than the number of months in this list
        divide by the number of values in the list of changes
    * The greatest increase in profits (date and amount) over the entire period
    * The greatest decrease in profits (date and amount) over the entire period

Your analysis should look similar to the following:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)

Your final script should both print the analysis to the terminal and export a text file with the results.
"""

import os #allows for us to use file pathing
import csv #allows for us to handle csv files

#create variables for the exercise
totalMonths = 0
totalProfLoss = 0
listOfChanges = []
listOfMonths = []
sumOfChanges = 0
averageChange = 0
greatestInc = 0
greatestIncMonth = ""
greatestDec = 0
greatestDecMonth = ""

# Store the file path associated with the file
budget_data_csv = os.path.join("Resources","budget_data.csv")

# Open the file and read it using the budget_data_csv file path
with open(budget_data_csv) as csvfile:

    #use csv.reader() function to open the file
    csvReader = csv.reader(csvfile, delimiter=",")

    # read the header row first
    header = next(csvReader)

    #go through the rows of data, starting at row 2
    for row in csvReader:

        #add the prof/loss for that row to the total prof/loss
        totalProfLoss += float(row[1])
        #subtract previous prof/loss from the current one
        if totalMonths == 0:
            difference = float(row[1])
            previousValue = difference
        else:
            difference = float(row[1])-previousValue
            previousValue = float(row[1]) 
            listOfChanges.append(difference)
        listOfMonths.append(row[0])
        #add 1 to the number of months
        totalMonths += 1

    #go through the values in listOfChanges
    monthIndex = 1
    for difference in listOfChanges:
        if difference > greatestInc:
            greatestInc = difference
            greatestIncMonth = listOfMonths[monthIndex]
        if difference < greatestDec:
            greatestDec = difference
            greatestDecMonth = listOfMonths[monthIndex]
        sumOfChanges += difference
        #averageChange = sumOfChanges/(totalMonths-1)
        averageChange = sumOfChanges/(totalMonths-1)
        monthIndex += 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalProfLoss: 0.0f}")
print(f"Average Change: ${averageChange: 0.2f}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")
