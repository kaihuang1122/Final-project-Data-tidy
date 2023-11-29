#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3

from datetime import datetime
import csv

with open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/weather_data.csv") as fin:
    table = list(csv.reader(fin))

new_table = []
for i in table:
    temp = datetime(2023, int(i[0]), int(i[1]), int(int(i[2])/60), int(int(i[2])%60), 0)
    epoch = int(temp.timestamp())
    for j in range(10):
        now_epoch = datetime.fromtimestamp(epoch+(j-5)*60)
        new_table.append([str(epoch+(j-5)*60), str(now_epoch.month), str(now_epoch.day), str(now_epoch.hour), str(now_epoch.minute), str(now_epoch.hour*60+now_epoch.minute)]+i[3:])


with open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/data.csv") as fin:
    control = list(csv.reader(fin))

for i in new_table:
    if int(i[0]) > 1701100740:
        control.append(i)

fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/Weatherdata.csv", "w")
fout.write("ID (Epoch timestamp), month, day, hour, minute, accumulated minutes, temperature, rainfall, relative humidity\n")
writer = csv.writer(fout)
writer.writerows(control)