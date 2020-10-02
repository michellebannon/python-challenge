# -*- coding: utf-8 -*-
"""


@author: mbannon
"""

#initialize variables
ProfitIncrease = 0
ProfitDecrease = 0
ProfitTotalSum = 0
AvgChange = 0
Change = 0
ProfitTotal = 0
profit = [] #list to contain all profits
MonthlyChange = []  #list to contain calculated change between months
BudgetData = {}
import csv

#open input file, read contents
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")
    next(csv_reader) #skip header
    MonthCount = 0
    MonthlyChange.append(Change) #set first month $ change to 0 
    for row in csv_reader: 
        ProfitTotal += int(row[1])
        profit.append(int(row[1]))        
        if MonthCount != 0: # don't calculate change if this is the first month (first row)
            Change = (int(profit[MonthCount]) - int(profit[MonthCount-1]))             
            MonthlyChange.append(Change)
            BudgetData[row[0]] = Change
        AvgChange += Change
        MonthCount += 1
csvfile.close

#find min and max amounts in monthly changes
ProfitDecrease = min(MonthlyChange)
ProfitIncrease = max(MonthlyChange)
#locate months that contain these values
for x, y in BudgetData.items():
    if ProfitDecrease == y:
        lowMonth = x
    if ProfitIncrease == y:
        highMonth = x

#print results
print('\nFinancial Analysis')
print('------------------------')
print(f'Total Months: {MonthCount}')
print(f'Total: ${ProfitTotal}')  
print(f'Average Change: ${(AvgChange/(MonthCount-1)):.2f}') #https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-30.php
print(f'Greatest Increase in Profits: {highMonth} (${ProfitIncrease})')
print(f'Greatest Decrease in Profits: {lowMonth} (${ProfitDecrease})')

#write FinancialAnalysis output file
filename = "C:\\Users\\mbannon\\Desktop\\python-challenge\\PyBank\\analysis\\FinancialAnalysis.txt"
with open(filename, 'w') as f:
    f.write('%s\n' % ("Financial Analysis"))
    f.write('%s\n' % ("------------------------"))
    f.write('%s%i\n' % ("Total Months: ", MonthCount))    
    f.write('%s%i\n' % ("Total: $", ProfitTotal))      
    f.write('%s%5.2f \n' % ("Average Change: $", (AvgChange/(MonthCount-1)))) #https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-30.php
    f.write('%s%s%s%i%s\n' % ("Greatest Increase in Profits: ", highMonth, " ($", ProfitIncrease, ")"))
    f.write('%s%s%s%i%s\n' % ("Greatest Decrease in Profits: ", lowMonth, " ($", ProfitDecrease, ")"))
f.close()