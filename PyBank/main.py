# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""
#import csv module
import csv

#define variables
ProfitIncrease = 0
ProfitDecrease = 0
AvgChange = 0
ProfitTotal = 0
i=0
date = []
profit = []

#store the file path associated with the file why doesn't this work?
#file = 'C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv'
#how do you sucessfully store the header row? I had to remove it because the count was wrong
#open the file and assign budget as a list

with open(r"C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    MonthCount = 0
    for row in csv_reader:
        ProfitTotal += int(row[1])
        MonthCount += 1
        print(row[0])
        
#net total amount of Profit/Losses" over the entire period



print()
print ()
print("Financial Analysis")
print("----------------------")
print(f'Total Months: {MonthCount}' )
print(f'Total: ${ProfitTotal}')
print(f"Average Change: ")
print(f"Greatest Increase in Profits:")
print(f"Greatest Decreate in Profits:")

