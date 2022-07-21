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
codexAmerican = codex['indv-rate-american']
codexAsian = codex['indv-rate-asian']
#print codex.csv
print(codex)

#write input variable occupancy rate
occupancyRate = input('Enter occupancy rate: ')
#print occupancy rate
print('Occupancy rate is: ' + occupancyRate)

#write occupancy rate into a new column in codex.csv
codex['occupancy-rate'] = occupancyRate
#print codex.csv
print(codex)

#save as codex-2.csv
codex.to_csv(r'C:\Users\tobia\Videos\REP3\profiler\codex-2.csv', index=False)
#print codex-2.csv
print(codex)

