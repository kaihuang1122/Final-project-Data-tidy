import csv
import numpy as np
from datetime import datetime
from tqdm import tqdm
total = dict()
for x in tqdm(open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()[0:]):
    
    capacity = int(open(f"/Users/kaihuang1122/Documents/ML/Final/Data tidy/1203version/{x[:-1]}.csv").readlines()[1].split(",")[-2])
    #for x in tqdm(["500119051 ", "500119075 "]):

    with open(f"/Users/kaihuang1122/Documents/ML/Final/Data tidy/1203version/{x[:-1]}.csv") as fin:
        table = [[[] for m in range(100)] for n in range(10)]
        reader = list(csv.reader(fin))[1:]
        for row in reader:
            weekday = int(row[3])
            mingroup = int((int(row[4])+10)/20)
            if mingroup == 72:
                mingroup == 0
            table[weekday][mingroup].append(row[-1])
        for w in range(7):
            for m in range(72):
                table[w][m] = [int(x) for x in table[w][m]]
                table[w][m] = np.mean(table[w][m])
        total[x] = (table)
        
fout = open(f"/Users/kaihuang1122/Documents/ML/Final/MLP GPT/average/touput.csv", "w")
fout.write("id,sbi\n")
writter = csv.writer(fout)
for p1 in [f"202310{x}" for x in [21, 22, 23, 24]]:
    for p2 in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
        for h in range(24):
            for m in [0, 20, 40]:
                weekday = datetime(2023, 10, int(p1[-2:])).weekday()
                out = [p1+'_'+p2[:-1]+"_%02d:%02d"%(h, m), total[x][weekday][int(h*3+m/20)]]
                writter.writerow(out)
                

for p1 in [f"202312{x}" for x in ["04", "05", "06", "07", "08", "09", "10"]]:
    for p2 in (open("/Users/kaihuang1122/Documents/ML/Final/html.2023.final.data/sno_test_set.txt").readlines()):
        for h in range(24):
            for m in [0, 20, 40]:
                weekday = datetime(2023, 12, int(p1[-2:])).weekday()
                out = [p1+'_'+p2[:-1]+"_%02d:%02d"%(h, m), total[x][weekday][int(h*3+m/20)]]
                writter.writerow(out)

        