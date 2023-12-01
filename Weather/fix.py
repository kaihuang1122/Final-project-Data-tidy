#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

from collections import deque
from datetime import datetime
import csv

fin = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/Weatherdata.csv")
table1 = list(csv.reader(fin))[1:]



prev = 0

for i in range(len(table1)-1):
    if i % 1440 != 0:
        table1[i][-2] = float(table1[i+1][-2]) - float(table1[i][-2])
    else:
        table1[i][-2] = float(table1[i-1][-2])
table2 = table1
table2[0][-2] = 0.0
dq = deque([])

for i in range(len(table2)):
    dq.append(table2[i][-2])
    table2[i][-2] = round(sum([float(x) for x in dq]), 1)
    if(len(dq) >= 60):
        dq.popleft()
table2[-1][-2] = 0.0


fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/fixeddata.csv", "w")
fout.write("ID, month, day, hour, minute, accumulated minutes, temperature, rainfall, relative humidity\n")
writter = csv.writer(fout)
writter.writerows(table2)