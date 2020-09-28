# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""

import csv
import os

candidates = []
i = 0
Winner = 0


#open the file
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
       VotesCount = 0
        for row in csv_reader:
            if row [2] == temp:
                
            VotesCount += 1
     
        
        
#find unique candidates


#do i first have to define it as a list? I CAN USE THIS ONCE I HAVE MY LIST OF CANDIDATES x = fruits.count("cherry") 
     
#Print Election Results
print()
print ()
print("Election Results")
print("-------------------------------")
print()
print(f'Total Votes: {VotesCount}' )
print()
print("-------------------------------")

print("-------------------------------")
print(f'Winner: {Winner}')
print("-------------------------------")