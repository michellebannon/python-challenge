# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""
#import csv module
import csv
import os

#initializing variables
ProfitIncrease = 0
ProfitDecrease = 0
AvgChange = 0
tmpChange = 0
ProfitSum = 0
i=0
date = [] #list to contain all dates
profit = [] #list to contain all profits
MonthlyChange = [] #list to contain calculated change between months

#how do you sucessfully store the header row? I had to remove it because the count was wrong

#open the file 
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    MonthCount = 0
    MonthlyChange.append(tmpChange) #set first mont record to 0
    for row in csv_reader:
        ProfitSum += int(row[1])
        date.append(row[0])
        profit.append(int(row[1]))
        #don't process if this is the first month (firstrow)
        if MonthCount != 0:
            tmpChange = (int(profit[MonthCount]) - int(profit[MonthCount-1]))
            MonthlyChange.append(tmpChange)
        AvgChange += tmpChange   
        MonthCount += 1
            
        print(row[0])
     
#test loop to verify lists
#i = 0
#for i in range(MonthCount-1):
#      print(f'Month: {date[i]}')
#      print(f'Profit: {profit[i]}')
#      print (f'Total Change: {MonthlyChange[i]}')
     
  
#net total amount of Profit/Losses" over the entire period

print()
print ()
print("Financial Analysis")
print("----------------------")
print(f'Total Months: {MonthCount}' )
print(f'Total: ${ProfitSum}')
print(f"Average Change: ")
print(f"Greatest Increase in Profits:")
print(f"Greatest Decreate in Profits:")

#export to txt file