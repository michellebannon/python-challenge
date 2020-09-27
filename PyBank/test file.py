# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:48:31 2020

@author: mbannon
"""

import csv
with open(r"C:\Users\mbannon\Desktop\python-challenge\PyBank\Resources\budget_data.csv") as csvfile:
    readCSV = csv.DictReader(csvfile)
    lines = csv.DictReader(csvfile)
    for line in lines:
        print(line)
        
    