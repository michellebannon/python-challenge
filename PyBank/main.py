# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""
#open the file and assign budget as a list
import csv
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    readCSV = csv.DictReader(csvfile)
    MonthCount = 0
    for row in readCSV:
        MonthCount += 1




print()
print ()
print("Financial Analysis")
print("----------------------")
print(f'Total Months: {MonthCount}' )
print(f"Total:")
print(f"Average Change: ")
print(f"Greatest Increase in Profits:")
print(f"Greatest Decreate in Profits:")

