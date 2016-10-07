__author__ = 'raghuveer'

import csv
import math
import matplotlib.pyplot as plt
import numpy
import scipy
from scipy.spatial.distance import pdist, squareform
from pylab import plot, show, savefig, xlim, figure,hold, ylim, legend, boxplot, setp, axes
from scipy.stats.stats import pearsonr
from collections import OrderedDict
import operator

flowerList = []
attList = []
class1List = []
class2List = []
class3List = []
wineCount = 178
class1 = 59
class2 = 71
class3 = 48

with open('wine.data', 'r') as f:
    flowers = csv.reader(f, delimiter=',')
    for row in flowers:
        row = map(float,row)
        flowerList.append(row)
f.close()


for x in flowerList:
    attList.append(map(float,x[1:]))

#print attList
def column(matrix, i):
    return [row[i] for row in matrix]

x = column(flowerList,1)

colAtt = []

for x in range(0,13):
    colAtt.append(column(attList,x))

totalAtt = []

for x in range(13):
    if(x==0):
        totalAtt.append(colAtt[0])
    if(x==1):
        totalAtt.append(colAtt[1])
    if(x==2):
        totalAtt.append(colAtt[2])
    if(x==3):
        totalAtt.append(colAtt[3])
    if(x==4):
        totalAtt.append(colAtt[4])
    if(x==5):
        totalAtt.append(colAtt[5])
    if(x==6):
        totalAtt.append(colAtt[6])
    if(x==7):
        totalAtt.append(colAtt[7])
    if(x==8):
        totalAtt.append(colAtt[8])
    if(x==9):
        totalAtt.append(colAtt[9])
    if(x==10):
        totalAtt.append(colAtt[10])
    if(x==11):
        totalAtt.append(colAtt[11])
    if(x==12):
        totalAtt.append(colAtt[12])



leastCorDict = {}
corDict = {}
pear = 0
for x in range(13):
    for y in range(13):
        if (x+1 is not y+1) and ((x+1,y+1) not in corDict.keys()) and ((y+1,x+1) not in corDict.keys()):
            pear = pearsonr(totalAtt[x],totalAtt[y])[0]
            pear = abs(pear)
            corDict.update({(x+1,y+1):pear})


ordered = OrderedDict(sorted(corDict.items(), key=lambda t: t[1]))
newA = dict(sorted(corDict.iteritems(), key=operator.itemgetter(1), reverse=True)[:4])
newB = dict(sorted(corDict.iteritems(), key=operator.itemgetter(1), reverse=False)[:4])
print newA
print newB



for key,val in newA.iteritems():
    plt.scatter(totalAtt[key[0]-1],totalAtt[key[1]-1])
    plt.show()

for key,val in newB.iteritems():
    plt.scatter(totalAtt[key[0]-1],totalAtt[key[1]-1])
    plt.show()
