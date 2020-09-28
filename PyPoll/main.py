# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 18:32:44 2020

@author: mbannon
"""
#open the file
import csv
import os

Winner = 0
#List = csv_reader do I need to define the data as a list to find the members

with open(r"C:\Users\mbannon\Desktop\python-challenge\PyPoll\Resources\election_data.csv") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)
    VotesCount = 0
    
    for row in csv_reader:
        VotesCount += 1
     

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