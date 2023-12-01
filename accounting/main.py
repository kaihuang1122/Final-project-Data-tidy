import matplotlib.pyplot as plt
import csv

fh = open("/Users/kaihuang1122/Documents/ML/Final/Data tidy/Weather/fixeddata.csv")
table = list(csv.reader(fh))
table = [float(x[-2]) for x in table[1:]]
print(table)

plt.hist(table)
plt.savefig("I")