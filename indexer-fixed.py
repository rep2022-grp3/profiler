import pandas as pd
import numpy as np
import os
import matplotlib as mpl

#setup baseline
#hotel limit index
maxFlowrateSPWH = float(500.0) #liters/30minutes
maxFlowrateAB = float(3500.0) #liters/30minutes
#load codex.csv [codex is sourced from RapidMiner hourly indexer]
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
#load codex-2.csv
codex2 = pd.read_csv(r'C:\Users\tobia\Videos\REP3\profiler\codex-2.csv')
#print codex-2.csv
print('This is codex-2.csv: ')
print(codex2)

#predict water demand
#in codex-2.csv, assign variable codex2-hour to first column, codexAmerican2 to second column, codexAsian2 to third column
codex2Hour = codex2['hour']
codex2American = codex2['indv-rate-american']
codex2Asian = codex2['indv-rate-asian']
codex2OccupancyRate = codex2['occupancy-rate']
#multiply codex2Asian by codex2OccupancyRate
codex2AsianDemand = codex2Asian * codex2OccupancyRate
#write codex2AsianDemand into a new column in codex2.csv
codex2['demand-Asian'] = codex2AsianDemand
#print codex2.csv
print(codex2)
#calculate the sum of codex2AsianDemand
sumCodex2AsianDemand = codex2['demand-Asian'].sum()
#simplify 2 digits after decimal point
sumCodex2AsianDemand = round(sumCodex2AsianDemand, 2)
#write maxFlowrateSPWH into a new column in codex-2.csv
codex2['max-flowrate-SPWH'] = maxFlowrateSPWH
#add time conversion to codex-2.csv
#multiply hour by 1800 to convert to seconds
codex2Second = codex2Hour * 3600
#add codex2Second to codex2.csv
codex2['second'] = codex2Second
#print codex-2.csv
print(codex2)
#print sumCodex2AsianDemand
print('Predicted demand for hot water today is: ' + str(sumCodex2AsianDemand) + ' liters')

#input depending variable: weather and boiler availability
#load weather-scrape.xlsx
weatherScrape = pd.read_excel(r'C:\Users\tobia\Videos\REP3\profiler\weather-scrape.xlsx')
#print weather-scrape.xlsx
print('This is weather-scrape.xlsx: ')
print(weatherScrape)
#assign variable weatherAvailability to the second column, spwhAvailability to the third column
weatherAvailability = weatherScrape['weather']
spwhAvailability = weatherScrape['spwh_available']
#combine weatherAvailability and spwhAvailability into a new columns in codex-2.csv
codex2['weather-availability'] = weatherAvailability
codex2['spwh-availability'] = spwhAvailability
#print codex-2.csv
print(codex2)

