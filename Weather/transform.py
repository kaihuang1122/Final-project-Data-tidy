import csv
from datetime import datetime
fin = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/1m_ins.csv")
table = list(csv.reader(fin))
def time(x):
    return datetime(int(x[0][0:4]), int(x[0][4:6]), int(x[0][6:8]), int(x[0][8:10]), int(x[0][10:12]))
table = [[int(time(x).timestamp()), time(x).month, time(x).day, time(x).hour, time(x).minute, time(x).hour*60+time(x).minute, time(x).hour*60+time(x).minute]+ x[-3:] for x in table]
print(table)
fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/predict.csv", "w")
fout.write("ID (Epoch timestamp), month, day, hour, minute, accumulated minutes, temperature, rainfall, relative humidity\n")
csv.writer(fout).writerows(table)