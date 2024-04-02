# Regular Python version of CreateData.ipynb

import numpy as np
import alphatensoralgos as at
from datetime import datetime
import pandas as pd
import sys

if len(sys.argv) < 5:
    print("Not enough arguments passed.\nSee README for details.")
    sys.exit()
elif int(sys.argv[2]) <= int(sys.argv[1]):
    print("Invalid values passed.\nSee README for details.")
    sys.exit()

min2 = int(sys.argv[1])
max2 = int(sys.argv[2])
max5 = int(sys.argv[3])
max4 = int(sys.argv[4])

two = 2 ** np.arange(min2,max2+1)
four = 4 ** np.arange(1,max4+1)
five = 5 ** np.arange(1,max5+1)

Fours = []
Fives = []

for i in two:
    fours = []
    for j in four:
        fours.append(i*j)
    Fours.append(fours)

    fives = []
    for j in five:
        fives.append(i*j)
    Fives.append(fives)

print(Fours)
print(Fives)


#log label array
lg2 = np.arange(min2,max2+1)
lg4 = np.arange(1,max4+1)
lg5 = np.arange(1,max5+1)

FoursDF = []
FivesDF = []
TwosDF = []
for i in lg2:
    for j in lg4:
        FoursDF.append(j)
        TwosDF.append(i)

    for j in lg5:
        FivesDF.append(j)


df5 = pd.DataFrame({'log2':TwosDF, 'log5':FivesDF})
df4 = pd.DataFrame({'log2':TwosDF, 'log4':FoursDF})

timefours = []
timefoursStr = []
timefoursnaive = []

for i in range(len(Fours)):  
    for j in Fours[i]:
        #create matrixes
        x = np.random.rand(j,j)
        y = np.random.rand(j,j)
        x = np.rint(x)
        y = np.rint(y)
        
        #run code for alphatensor
        cur = datetime.now()
        at.matMul(x,y,True)
        delta = datetime.now() - cur
        timefours.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(x.astype(bool),y.astype(bool),True)
        delta = datetime.now() - cur
        timefoursStr.append(delta)

        #run regular naive
        cur = datetime.now()
        at.naiveSquare(x.astype(bool),y.astype(bool))
        delta = datetime.now() - cur
        timefoursnaive.append(delta)

fourTimes = pd.DataFrame({'NaiveTimes':timefoursnaive,'StrassenTimes':timefoursStr,'AlphaTensor':timefours})

fourTimes['NaiveTimes'] = fourTimes['NaiveTimes'].apply(lambda x: x.total_seconds())
fourTimes['StrassenTimes'] = fourTimes['StrassenTimes'].apply(lambda x: x.total_seconds())
fourTimes['AlphaTensor'] = fourTimes['AlphaTensor'].apply(lambda x: x.total_seconds())

DF4 = pd.concat([fourTimes, df4], axis=1)
DF4.to_csv("log4.csv",index=False)

print("log4 saved to file")

timefives = []
timefivesStr = []
timefivesnaive= []

for i in range(len(Fives)):  
    #do same for fives
    for j in Fives[i]:
        #create matrixes
        x = np.random.randint(0,5,size=(j,j))
        y = np.random.randint(0,5,size=(j,j))
        
        #run code for alphatensor
        cur = datetime.now()
        at.matMul(x,y,False)
        delta = datetime.now() - cur
        timefives.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(x,y,False)
        delta = datetime.now() - cur
        timefivesStr.append(delta)

        #run regular naive
        cur = datetime.now()
        x @ y
        delta = datetime.now() - cur
        timefivesnaive.append(delta)

fivesTimes = pd.DataFrame({'NaiveTimes':timefivesnaive,'StrassenTimes':timefivesStr,'AlphaTensor':timefives})

fivesTimes['NaiveTimes'] = fivesTimes['NaiveTimes'].apply(lambda x: x.total_seconds())
fivesTimes['StrassenTimes'] = fivesTimes['StrassenTimes'].apply(lambda x: x.total_seconds())
fivesTimes['AlphaTensor'] = fivesTimes['AlphaTensor'].apply(lambda x: x.total_seconds())

DF5 = pd.concat([fivesTimes, df5], axis=1)
DF5.to_csv("log5.csv",index=False)

print("log5 saved to file.")