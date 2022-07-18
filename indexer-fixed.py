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
occupancyRate = float(input('Enter occupancy rate: '))
#print occupancy rate
print('Occupancy rate is: ' + occupancyRate)

#multiply codexAsian by occupancyRate
demandAsian = codexAsian * float(occupancyRate)
#put demandAsian by hour in dataframe
demandAsianByHour = pd.DataFrame(demandAsian, index=hour, columns=['demand-asian'])
#print demandAsianByHour
print(demandAsianByHour)