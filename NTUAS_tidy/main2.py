from datetime import datetime
import csv
import tqdm


MNIN = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/MN.csv")
MN = list(csv.reader(MNIN))
MNR2IN = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/MNR2.csv")
MNR2 = list(csv.reader(MNR2IN))
counting = 0
table = []
epoch = (datetime(2023, 10, 2, 0, 0, 0))

fout = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/NTUAS_tidy/Total/data.csv", "w")
writter = csv.writer(fout)

while epoch.timestamp() <= datetime(2023, 11, 28, 0, 0, 0).timestamp():
    if epoch.strftime("%Y%m%d%H%M")[-4:] != "0000":
        str = epoch.strftime("%Y%m%d%H%M")
    else:
        temp = datetime.fromtimestamp(epoch.timestamp()-86400)
        str = temp.strftime("%Y%m%d24%M")
    if(str[8:10] == "00"):
        str[8:10] == "24"
    temp = [int(epoch.timestamp()), epoch.month, epoch.day, epoch.hour, epoch.minute, epoch.hour*60+epoch.minute]
    print(str)
    prev = 0
    temp2 = [-1, -1, -1]
    for j in MN:
        #print(j[0])
        if(str == j[0]):
            temp2[0] = j[1]
            temp2[2] = j[2]
            break
        
    for j in MNR2:

        #print(j[0])
        if(str == j[0]):
            temp2[1] = float(j[1]) - prev
            prev = float(j[1])
            break
    
    if temp2[0] == -1:
        temp2[0] = table[-3]
        counting+=1
    if temp2[1] == -1:
        temp2[1] = table[-2]
        counting+=1
    if temp2[2] == -1:
        temp2[2] = table[-1]
        counting+=1

    if -1 in temp2:
        break

    writter.writerow(temp+temp2)
    table = (temp+temp2)
    epoch = datetime.fromtimestamp(epoch.timestamp()+60)

print(counting)

