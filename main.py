#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import json
import sys
import os
import numpy as np
from datetime import datetime
import csv
def week_convert(month, day):
    return str(datetime(2023, month, day).weekday())
target = np.loadtxt("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt")
prifix = "/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/release/2023"
month = ["10", "11"]
day10 = ["%02d"% x for x in list(range(2, 12))+list(range(15,21))+list(range(25, 32))]
day10 = [["10", x] for x in day10]
day11 = ["%02d"% x for x in range(1,int(sys.argv[1]))]
day11 = [["11", x] for x in day11]
mid = "/"
target = list(target)
suffix = ".json"


my_prifix = "/Users/kaihuang1122/Documents/ML/Final/Data tidy/11"+sys.argv[1]+"version"
for port in target:
    port_fh = open(my_prifix+"/"+str(int(port))+".csv", "w")
    writter = csv.writer(port_fh)
    port_fh.write("ID, month, day, weekday, accumulated minutes, capacity, bike amount\n")
    for day in day10+day11:
        #print(day, int(port))
        with open(prifix+day[0]+day[1]+mid+str(int(port))+suffix) as fh:
            data = json.load(fh)
        temp_mdw = [day[0], int(day[1]), week_convert(int(day[0]), int(day[1]))]
        #mdw = day[0]+','+str(int(day[1]))+','+week_convert(int(day[0]), int(day[1]))+','
        for hour in range(24):
            for minute in range(60):
                temp = data["%02d:%02d"%(hour, minute)]
                if "tot" in temp:
                    temp_mpc = [hour*60+minute, temp["tot"], temp["sbi"]]
                    writter.writerow([int(datetime(2023, int(day[0]), int(day[1]), hour, minute).timestamp())]+temp_mdw+temp_mpc)
                    #mpc = str(hour*60+minute)+','+str(temp["tot"])+','+str(temp["sbi"])
                    #port_fh.write(mdw+mpc+'\n')    
    port_fh.close()