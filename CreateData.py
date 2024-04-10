# Regular Python version of CreateData.ipynb

import numpy as np
import alphatensoralgos as at
from datetime import datetime
import pandas as pd
import sys


import loading
import os
os.system("")

if len(sys.argv) < 4:
    print("Not enough arguments passed.\nSee README for details.")
    sys.exit()
elif int(sys.argv[2]) <= int(sys.argv[1]):
    print("Invalid values passed.\nSee README for details.")
    sys.exit()

animation: loading.TermLoading = loading.TermLoading.shared()
animation.show('Multiplying matrixes...', finish_message='Times saved to csv.')

min2 = int(sys.argv[1])
max2 = int(sys.argv[2])
maxnums = int(sys.argv[3])

two = 2 ** np.arange(min2,max2+1)
four = 4 ** np.arange(1,maxnums+1)
five = 5 ** np.arange(1,maxnums+1)
three = 3 ** np.arange(1,maxnums+1)

Fours = []
Fives = []
Threes = []

for i in two:
    fours = []
    for j in four:
        fours.append(i*j)
    Fours.append(fours)

    fives = []
    for j in five:
        fives.append(i*j)
    Fives.append(fives)

    threes = []
    for j in three:
        threes.append(i*j)
    Threes.append(threes)



#log label array
lg2 = np.arange(min2,max2+1)
lg4 = np.arange(1,maxnums+1)
lg5 = np.arange(1,maxnums+1)
lg5mod2 = np.arange(1,maxnums+1)
lg345 = np.arange(1,maxnums+1)
lg445 = np.arange(1,maxnums+1)
lg445mod2 = np.arange(1,maxnums+1)
lg455 = np.arange(1,maxnums+1)

df2 = []
dflen = []
for i in lg2:
    for j in lg4:
        dflen.append(j)
        df2.append(i)


df5 = pd.DataFrame({'log2':df2, 'log5':dflen})
df4 = pd.DataFrame({'log2':df2, 'log4':dflen})
df345 = pd.DataFrame({'log2':df2, 'log345':dflen})
df445 = pd.DataFrame({'log2':df2, 'log445':dflen})
df455 = pd.DataFrame({'log2':df2, 'log455':dflen})


timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
    for j in range(len(Threes[i])):
        #create matrixes
        x = Threes[i][j]
        y = Fours[i][j]
        z = Fives[i][j]
        a = np.random.randint(0,5,size=(x,y))
        b = np.random.randint(0,5,size=(y,z))

        #run code for alphatensor
        cur = datetime.now()
        at.mat345(a,b,lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(a,b,False)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        a @ b
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df345], axis=1)
DF.to_csv("log345.csv",index=False)

print("log345 saved to file")

timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
     for j in range(len(Threes[i])):
        #create matrixes
        x = Fours[i][j]
        y = Fours[i][j]
        z = Fives[i][j]
        a = np.random.randint(0,5,size=(x,y))
        b = np.random.randint(0,5,size=(y,z))
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat445(a,b,lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(a,b,False)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        a @ b
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df445], axis=1)
DF.to_csv("log445.csv",index=False)


timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
    for j in range(len(Threes[i])):
        #create matrixes
        x = Fours[i][j]
        y = Fours[i][j]
        z = Fives[i][j]
        a = np.random.rand(x,y)
        b = np.random.rand(y,z)
        a = np.rint(a)
        b = np.rint(b)
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat445mod2(a.astype(bool),b.astype(bool),lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(a.astype(bool),b.astype(bool),True)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        at.naiveRect(a.astype(bool),b.astype(bool),len(a),len(b),len(b[0]))
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df445], axis=1)
DF.to_csv("log445mod2.csv",index=False)


timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
     for j in range(len(Threes[i])):
        #create matrixes
        x = Fours[i][j]
        y = Fives[i][j]
        z = Fives[i][j]
        #create matrixes
        a = np.random.randint(0,5,size=(x,y))
        b = np.random.randint(0,5,size=(y,z))
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat455(a,b,lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(a,b,False)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        a @ b
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df455], axis=1)
DF.to_csv("log455.csv",index=False)


timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
   for j in range(len(Fours[i])):
        #create matrixes
        k = Fours[i][j]
        x = np.random.rand(k,k)
        y = np.random.rand(k,k)
        x = np.rint(x)
        y = np.rint(y)
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat444mod2(x.astype(bool),y.astype(bool),lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(x.astype(bool),y.astype(bool),True)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        at.naiveSquare(x.astype(bool),y.astype(bool))
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df4], axis=1)
DF.to_csv("log444mod2.csv",index=False)


timeAt = []
timeStr = []
timeNaive= []

for i in range(len(Fives)):  
    #do same for fives
    for j in range(len(Fives[i])):
        #create matrixes
        k = Fives[i][j]
        x = np.random.randint(0,5,size=(k,k))
        y = np.random.randint(0,5,size=(k,k))
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat555(x,y,lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(x,y,False)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        x @ y
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df5], axis=1)
DF.to_csv("log555.csv",index=False)

timeAt = []
timeStr = []
timeNaive = []

for i in range(len(two)):  
    for j in range(len(Fives[i])):
        #create matrixes
        k = Fives[i][j]
        x = np.random.rand(k,k)
        y = np.random.rand(k,k)
        x = np.rint(x)
        y = np.rint(y)
        
        #run code for alphatensor
        cur = datetime.now()
        at.mat555mod2(x.astype(bool),y.astype(bool),lg4[j])
        delta = datetime.now() - cur
        timeAt.append(delta)
        
        #run regular strassen
        cur = datetime.now()
        at.strassenInit(x.astype(bool),y.astype(bool),True)
        delta = datetime.now() - cur
        timeStr.append(delta)

        #run regular naive
        cur = datetime.now()
        at.naiveSquare(x.astype(bool),y.astype(bool))
        delta = datetime.now() - cur
        timeNaive.append(delta)

times = pd.DataFrame({'NaiveTimes':timeNaive,'StrassenTimes':timeStr,'AlphaTensor':timeAt})

times['NaiveTimes'] = times['NaiveTimes'].apply(lambda x: x.total_seconds())
times['StrassenTimes'] = times['StrassenTimes'].apply(lambda x: x.total_seconds())
times['AlphaTensor'] = times['AlphaTensor'].apply(lambda x: x.total_seconds())

DF = pd.concat([times, df5], axis=1)
DF.to_csv("log555mod2.csv",index=False)

animation.finished = True