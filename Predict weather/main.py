import numpy as np
from datetime import datetime
import csv

table = np.loadtxt("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Predict weather/2023113000_forecast.txt")
print(table)
#ID, month, day, hour, minute, accumulated minutes, temperature, rainfall, relative humidity
new = []
for row in table:
    time = str(int(row[0]))
    time = datetime(2023,int(time[4:6]), int(time[6:8]), int(time[8:10]), int(time[10:12]))
    
    for i in range(360):
        temp = datetime.fromtimestamp(time.timestamp()-180+i*60)
        #print(temp)
        temp = [int(temp.timestamp()), temp.month, temp.day, temp.hour, temp.minute, temp.hour*60+temp.minute, row[-3], row[-2], row[-1]]
        new.append(temp)

fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Predict weather/2023113000_forecast.csv", "w")
fout.write("ID, month, day, hour, minute, accumulated minutes, temperature, rainfall, relative humidity\n")
writter = csv.writer(fout)
writter.writerows(new)