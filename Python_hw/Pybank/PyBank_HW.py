#create file paths across operating systems
import os
# Module for reading CSV files
import csv
csvpath = os.path.join('Pybank/Resources/budget_data.csv')

# making list variables
Date = []
total_profit_loss = []
profit_loss_change = []

# look through PyBankFile-data
with open(csvpath, 'r') as PyBankFile:
    # seperate information with "," as key figure
    csv_reader = csv.reader(PyBankFile, delimiter=",")
    csv_header = next(PyBankFile)
    
    # look through date rows
    for row in csv_reader:
        Date.append(row[0])
        # make total_profit_loss a interger
        total_profit_loss.append(int(row[1]))    
        
     #look through Profit/Loss
    for i in range(len(total_profit_loss)-1):
        profit_loss_change.append(total_profit_loss[i+1]-total_profit_loss[i])

# Formulas
# obtaining the aearge
average_profit_change = round(sum(profit_loss_change)/ len(profit_loss_change),2)
# Obtaining the Max profit/loss
maximum = max(profit_loss_change)
# Obtaining the min profit/loss
minimum = min(profit_loss_change)
# Obtaining the Date for Max profit/loss
date_maximum = Date[profit_loss_change.index(maximum)+1]
# Obtaining the Date for Min profit/loss
date_minimum = Date[profit_loss_change.index(minimum)+1]

#print out table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Date)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: {average_profit_change}")
print(f"Greatest Increase in Profits: {date_maximum} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {date_minimum} (${(str(minimum))})")

# Print table onto a text file
csvpath2 = os.path.join('PyBank/Analysis/Pybank_Analysis.txt')
with open(csvpath2, "w", newline = "") as text:
    text.write("\n")
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write(f"Total Months: {len(Date)}\n")
    text.write(f"Total: ${sum(total_profit_loss)}\n")
    text.write(f"Average Change: ${average_profit_change}\n")
    text.write(f"Greatest Increase in Profits: {date_maximum} (${maximum})\n")
    text.write(f"Greatest Decrease in Profits: {date_minimum} (${minimum})\n")