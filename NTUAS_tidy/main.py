import csv
MNR2 = []
MN = []

for day in range(31):
    pathname = "202310%02d.txt"%(day+1)
    with open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_20231001-20231127/"+pathname) as fin:
        table = list(fin.readlines())



    for string in table:
        temp = list(string.split(",")) + [0,0,0,0,0,0,0]
        if("MNR2," in string):
            MNR2.append(temp[3:5])
        elif("MN,2023" in string):
            MN.append([temp[3], temp[6], temp[8]])

    #print(MNR2)
    #print(MN)
for day in range(27):
    pathname = "202311%02d.txt"%(day+1)
    with open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_20231001-20231127/"+pathname) as fin:
        table = list(fin.readlines())



    for string in table:
        temp = list(string.split(",")) + [0,0,0,0,0,0,0]
        if("MNR2," in string):
            MNR2.append(temp[3:5])
        elif("MN,2023" in string):
            MN.append([temp[3], temp[6], temp[8]])

    #print(MNR2)
    #print(MN)
    
fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/MNR2.csv", "w")
writter = csv.writer(fout)
for i in range(len(MNR2)):
    writter.writerow(MNR2[i])
fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/MN.csv", "w")
writter = csv.writer(fout)
for i in range(len(MN)):
    writter.writerow(MN[i])

