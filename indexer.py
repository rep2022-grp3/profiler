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

#variable 1 --> occupants
#data input
print("insert hotel occupancy rate")
occupancyRate = float(input())
print("hotel occupancy rate is", occupancyRate)
#profile config
print("all of the guests are Asian")
#modify this later for racial profiling

#determine water volume profile
#create new variable volumeDemandAsian, multiply occupancyRate with codexAsian, create new csv with hour and volumeDemandAsian
volumeDemandAsian = occupancyRate * codexAsian
volumeDemandAsian = pd.DataFrame(volumeDemandAsian)
volumeDemandAsian.columns = ['volumeDemandAsian']
volumeDemandAsian['hour'] = hour
volumeDemandAsian.to_csv(r'C:\Users\tobia\Videos\REP3\profiler\volumeDemandAsian.csv')
#create new variable volumeDemandAmerican, multiply occupancyRate with codexAmerican, create new csv with hour and volumeDemandAmerican
#volumeDemandAmerican = occupancyRate * codexAmerican
#volumeDemandAmerican = pd.DataFrame(volumeDemandAmerican)
#volumeDemandAmerican.columns = ['volumeDemandAmerican']
#volumeDemandAmerican['hour'] = hour
#volumeDemandAmerican.to_csv(r'C:\Users\tobia\Videos\REP3\profiler\volumeDemandAmerican.csv')

#import volumeDemandAsian.csv as codexNew and create line graph
codexNew = pd.read_csv(r'C:\Users\tobia\Videos\REP3\profiler\volumeDemandAsian.csv')
codexNew.plot(x='hour', y='volumeDemandAsian')
mpl.pyplot.show()

