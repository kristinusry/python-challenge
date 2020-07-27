# Load dependencies
import os
import csv

# Define file path
csvpath = os.path.join("03-PYTHON", "Homework", "python-challenge", "PyBank", "Resources", "budget_data.csv")

# Define variables
totalMonths = 0
totalProfit = 0
previousMonth = 0
currentMonth = 0
profitChange = 0

# Create lists
monthsList = []
profitChangeList = []

#Call file
with open(csvpath) as csvfile:
    # Read file
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvreader)   
    
    # Read through each row of data after the header
    for row in csvreader:

        # Find total months and total sum
        # ---------------------------------------------------------------------------
        # The total number of months included in the dataset
        totalMonths += 1

        # The net total amount of "Profit/Losses" over the entire period (sum of earnings)
        totalProfit += int(row[1])
        # ---------------------------------------------------------------------------

        # Find current month value
        currentMonth = int(row[1])

        if (totalMonths == 1):
            # For first row set the value of previous month to be current month
            previousMonth = currentMonth

        else:

            # Calculate month-to-month change and append to lists
            # ---------------------------------------------------------------------------
            # Find difference between current month and the previous month
            profitChange = currentMonth - previousMonth

            # Append each profit change amount to the profit change list
            profitChangeList.append(profitChange)

            # Reset for next loop
            previousMonth = currentMonth

            # Add month to months list for index search
            monthsList.append(row[0])
            # ---------------------------------------------------------------------------

    # The average of the changes in profit change list over the entire period
    # ---------------------------------------------------------------------------
    def average(profitChangeList):
        length = len(profitChangeList)
        total = 0.00
        for number in profitChangeList:
            total += number
        return total / length

    # Average and round the result:
    averageProfit = average(profitChangeList)
    averageProfit = round(averageProfit, 2)
    # ---------------------------------------------------------------------------

    # Find the greatest increase and decrease month and amount (use index)
    # ---------------------------------------------------------------------------    
    highestNumber = max(profitChangeList)
    if highestNumber is highestNumber:
        highestNumberMonth = profitChangeList.index(highestNumber)

    lowestNumber = min(profitChangeList)
    if lowestNumber is lowestNumber:
        lowestNumberMonth = profitChangeList.index(lowestNumber)
    
    greatestIncreaseMonth = monthsList[highestNumberMonth]
    greatestDecreaseMonth = monthsList[lowestNumberMonth]
    # ---------------------------------------------------------------------------
        
    #Print out all results in terminal
    # ---------------------------------------------------------------------------
    nl = '\n'
    print(f'Financial Analysis{nl}------------------------------{nl}Total Months: {totalMonths}{nl}Total: ${totalProfit} {nl}Average Change: ${averageProfit} {nl}Greatest Increase in Profits: {greatestIncreaseMonth} (${highestNumber}){nl}Greatest Decrease in Profits: {greatestDecreaseMonth} (${lowestNumber})')
    # ---------------------------------------------------------------------------

#Create text file in Analysis folder
# ---------------------------------------------------------------------------
output_path = os.path.join("03-PYTHON", "Homework", "python-challenge", "PyBank", "Analysis", "budget_results.txt")
write_file = open(output_path, 'w+')
write_file.write(f'Financial Analysis' + '\n')
write_file.write(f'------------------------------' + '\n')
write_file.write(f'Total Months: {totalMonths}' + '\n')
write_file.write(f'Total: ${totalProfit}' + '\n')
write_file.write(f'Average Change: ${averageProfit}' + '\n')
write_file.write(f'Greatest Increase in Profits: {greatestIncreaseMonth} (${highestNumber})' + '\n')
write_file.write(f'Greatest Decrease in Profits: {greatestDecreaseMonth} (${lowestNumber}')
# ---------------------------------------------------------------------------

