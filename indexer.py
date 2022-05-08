from re import U
import pandas as pd
import numpy as np
import os
import matplotlib as mpl

#hotel limit index
maxFlowrateSPWH = float(500.0) #liters/30minutes
maxFlowrateAB = float(3500.0) #liters/30minutes

#load codex.csv
codex = pd.read_csv(r'C:\Users\tobia\Videos\REP3\profiler\codex.csv')
#assign variable codex-hour to first column, codexAmerican to second column, codexAsian to third column
hour = codex['hour']
codexAmerican = codex['american']
codexAsian = codex['asian']

#variable 1 --> occupants
#data input
print("insert hotel occupancy rate")
occupancyRate = float(input())
print("hotel occupancy rate is", occupancyRate)
#profile config
print("all of the guests are Asian")
#modify this later for racial profiling

#determine water volume profile
