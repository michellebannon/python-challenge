# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""

import csv
import operator
import os
DEBUG = False
temp = ""
candidatevotes = []
candidates = []
i = 0
Winner = 0
tempvotes = 0
tempcandidate = ""

#open the file
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    results = sorted(csv_reader,key=operator.itemgetter(2))     #how to sort csv https://www.youtube.com/watch?v=VvKn3Y7qAKs
    VotesCount = 0
    for row in results:
        VotesCount += 1
        tempvotes += 1
        if row[2] != tempcandidate:   #find unique candidates
          tempcandidate = row[2]
          candidates.append(tempcandidate)  #save new candidate name        
          if VotesCount != 1:
              candidatevotes.append(tempvotes)          
              tempvotes = 0
               
candidatevotes.append(tempvotes) #save the last candidates vote total
    
             
        
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