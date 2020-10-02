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
candidatelist = []
candidates = {}
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
        candidate = row[2]
        VotesCount += 1
        tempvotes += 1
        if candidate not in candidates:   #find unique candidates
            candidates[candidate] = 0 #save new candidate name
            candidatelist.append(candidate)
        candidates[candidate] += 1
               
#candidatevotes.append(tempvotes) #save the last candidates vote total
#Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)  
#calculate the % of votes for each candidate          
        


#Print Election Results
print(candidates)
print(candidatelist)
print("Election Results")
print("-------------------------------")
print()
print("Total Votes: " + str(VotesCount) )
print()
print("-------------------------------")
#print(f"{candidates['Khan'].key()}")
print("-------------------------------")
print("Winner: ")
print("-------------------------------")