"""""
Script to run analysis for the PyBank Data.

A Python script that analyzes the financial records from a set of financial data called budget_data.csv.

This script will analyze the records and calculate the following:
1. The total number of months included in the dataset.
2. The net total amount of "Profit/Losses" over the entire period.
3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes.
4. The greatest increase in profits (date and amount) over the entire period.
5. The greatest decrease in losses (date and amount) over the entire period.

Author: Abayomi Olujobi
"""

import os
import csv
path = "/Users/abayomi/GitHubs/Python-Challenge/PyBank/"
budget_data = os.path.join(path,"Resources", "budget_data.csv")

def currency(amount):
    #Changes the amount to currency format
    currency_format = "${:,.2f}".format(amount)
    return currency_format

def merge(list_1, list_2):
    #Merges two lists into nested tuples
    nested_tuples = tuple(zip(list_1, list_2))
    return nested_tuples

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    counts = 0
    total = 0
    list_amount = []
    dates = []
    for row in csvreader:
        
        #counting the total number of months in the dataset (i.e. rows)
        counts += 1
        
        #calculating the total number of profits/losses in the second column
        total += int(row[1])
        
        #converting Profit/Losses column into a list
        list_amount.append(int(row[1]))

        #converting Date column into a list
        dates.append(str(row[0]))
        
    print('Financial Analysis')
    print('----------------------')
    
    #list comprehension that subtracts the current value from the next value 
    profit_diff = [j - i for i, j in zip(list_amount, list_amount[1:])]

    #Print Total number of months
    print(f'Total Months: {counts}')

    #Print Total
    print(f'Total: {currency(total)}')
    
    #Calculate and print average change
    sum_list = sum(profit_diff)
    average_change = sum_list/len(profit_diff)
    print(f'Average Change: {currency(average_change)}')

    sorted_profit_diff = sorted(profit_diff)
    sorted_profit_diff.insert(0,0)
    highest_value = sorted_profit_diff[-1]
    lowest_value = sorted_profit_diff[1]

    outer_tuple = merge(dates[1:], profit_diff)

    for x in range(len(outer_tuple)):
        if highest_value in outer_tuple[x]:
            highest_value_date = outer_tuple[x][0]
        if lowest_value in outer_tuple[x]:
            lowest_value_date = outer_tuple[x][0]

    #Print greatest increase in profit
    print(f'Greatest Increase in Profits: {highest_value_date} ({currency(highest_value)})')

    #Print greatest decrease in profit
    print(f'Greatest Decrease in Profits: {lowest_value_date} ({currency(lowest_value)})')

    #Export a text file with the results
    path2 = "/Users/abayomi/GitHubs/Python-Challenge/PyBank/Analysis/"
    file_name = 'analysis.txt'
    complete_name = os.path.join(path2,file_name)

    f = open(complete_name, 'w')
    f.write('Financial Analysis\n----------------------\n')
    f.write(f'Total Months: {counts}\n')
    f.write(f'Total: {currency(total)}\n')
    f.write(f'Average Change: {currency(average_change)}\n')
    f.write(f'Greatest Increase in Profits: {highest_value_date} ({currency(highest_value)})\n')
    f.write(f'Greatest Decrease in Profits: {lowest_value_date} ({currency(lowest_value)})')
    
    f.close()

    










    

    

