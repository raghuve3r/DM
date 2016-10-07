__author__ = 'raghuveer'

import csv
import math
import matplotlib.pyplot as plt
import numpy
from pylab import plot, show, savefig, xlim, figure,hold, ylim, legend, boxplot, setp, axes



flowerList = []
setosa = []
versicolor = []
verginica = []

with open('iris1.data', 'r') as f:
    flowers = csv.reader(f, delimiter=',')
    for row in flowers:
        flowerList.append(row)
f.close()

def meanAndSD(x):
    meanFeature = 0
    countFeature = 0
    sumFeature = 0
    sqr = 0
    diff = 0
    var = 0
    sd = 0
    for s in flowerList:
        sumFeature = sumFeature + float(s[x])
        countFeature = countFeature + 1
    meanFeature = sumFeature/countFeature
    for s in flowerList:
        diff = float(s[x]) - meanFeature
        diff = diff * diff
        sqr = sqr + diff
    var = sqr/countFeature
    sd = math.sqrt(var)
    print 'Mean for feature ' + str(x+1) + ' is ' + str(meanFeature)
    print 'Standard deviation for feature ' + str(x+1) + ' is ' + str(sd)



def meanAndSDFlower(x,y):
    meanFeature = 0
    countFeature = 0
    sumFeature = 0
    sqr = 0
    diff = 0
    var = 0
    sd = 0
    if(x==0):
        for s in setosa:
            sumFeature = sumFeature + float(s[y])
            countFeature = countFeature + 1
        meanFeature = sumFeature/countFeature
        for s in setosa:
            diff = float(s[y]) - meanFeature
            diff = diff * diff
            sqr = sqr + diff
        var = sqr/countFeature
        sd = math.sqrt(var)
        print "Mean for setosa's feature " + str(y+1) + ' is ' + str(meanFeature)
        print "Standard deviation for setosa's feature " + str(y+1) + ' is ' + str(sd)
    elif(x==1):
        for s in versicolor:
            sumFeature = sumFeature + float(s[y])
            countFeature = countFeature + 1
        meanFeature = sumFeature/countFeature
        for s in versicolor:
            diff = float(s[y]) - meanFeature
            diff = diff * diff
            sqr = sqr + diff
        var = sqr/countFeature
        sd = math.sqrt(var)
        print "Mean for versicolor's feature " + str(y+1) + ' is ' + str(meanFeature)
        print "Standard deviation for versicolor's feature " + str(y+1) + ' is ' + str(sd)
    else:
        for s in verginica:
            sumFeature = sumFeature + float(s[y])
            countFeature = countFeature + 1
        meanFeature = sumFeature/countFeature
        for s in verginica:
            diff = float(s[y]) - meanFeature
            diff = diff * diff
            sqr = sqr + diff
        var = sqr/countFeature
        sd = math.sqrt(var)
        print "Mean for verginica's feature " + str(y+1) + ' is ' + str(meanFeature)
        print "Standard deviation for verginica's feature " + str(y+1) + ' is ' + str(sd)

for y in range(4):
    meanAndSD(y)

for s in flowerList:
    if(s[4] == 'Iris-setosa'):
        setosa.append(s)
    elif(s[4] == 'Iris-versicolor'):
        versicolor.append(s)
    else:
        verginica.append(s)

for y in range(3):
    for z in range(4):
        meanAndSDFlower(y,z)

setosaPlot1 = []
versicolorPlot1 = []
verginicaPlot1 = []

setosaPlot2 = []
versicolorPlot2 = []
verginicaPlot2 = []

setosaPlot3 = []
versicolorPlot3 = []
verginicaPlot3 = []

setosaPlot4 = []
versicolorPlot4 = []
verginicaPlot4 = []

for x in setosa:
    setosaPlot1.append(float(x[0]))
    setosaPlot2.append(float(x[1]))
    setosaPlot3.append(float(x[2]))
    setosaPlot4.append(float(x[3]))

for x in versicolor:
    versicolorPlot1.append(float(x[0]))
    versicolorPlot2.append(float(x[1]))
    versicolorPlot3.append(float(x[2]))
    versicolorPlot4.append(float(x[3]))

for x in verginica:
    verginicaPlot1.append(float(x[0]))
    verginicaPlot2.append(float(x[1]))
    verginicaPlot3.append(float(x[2]))
    verginicaPlot4.append(float(x[3]))

setosaPlot1 = numpy.array(setosaPlot1)
versicolorPlot1 = numpy.array(versicolorPlot1)
verginicaPlot1 = numpy.array(verginicaPlot1)


setosaPlot2 = numpy.array(setosaPlot2)
versicolorPlot2 = numpy.array(versicolorPlot2)
verginicaPlot2 = numpy.array(verginicaPlot2)


setosaPlot3 = numpy.array(setosaPlot3)
versicolorPlot3 = numpy.array(versicolorPlot3)
verginicaPlot3 = numpy.array(verginicaPlot3)


setosaPlot4 = numpy.array(setosaPlot4)
versicolorPlot4 = numpy.array(versicolorPlot4)
verginicaPlot4 = numpy.array(verginicaPlot4)

data1 = [setosaPlot1,versicolorPlot1, verginicaPlot1]
data2 = [setosaPlot2,versicolorPlot2, verginicaPlot2]
data3 = [setosaPlot3,versicolorPlot3, verginicaPlot3]
data4 = [setosaPlot4,versicolorPlot4, verginicaPlot4]
fs=10
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(30, 10))
labels = list('Setosa Versicolor Virginica')
axes[0].boxplot(data1)
axes[0].set_xticklabels(['Setosa','Versicolor','Virginica'])
axes[0].set_ylim([4,8])
axes[0].set_ylabel('Sepal length in cms')
axes[0].set_title('Sepal length', fontsize=fs)

axes[1].boxplot(data2)
axes[1].set_xticklabels(['Setosa','Versicolor','Virginica'])
axes[1].set_ylim([1,4.5])
axes[1].set_ylabel('Sepal width in cms')
axes[1].set_title('Sepal width', fontsize=fs)

axes[2].boxplot(data3)
axes[2].set_xticklabels(['Setosa','Versicolor','Virginica'])
axes[2].set_ylim([1,7])
axes[2].set_ylabel('Petal length in cms')
axes[2].set_title('Petal length', fontsize=fs)

axes[3].boxplot(data4)
axes[3].set_xticklabels(['Setosa','Versicolor','Virginica'])
axes[3].set_ylim([0,3])
axes[3].set_ylabel('Petal width in cms')
axes[3].set_title('Petal width', fontsize=fs)

for ax in axes.flatten():
    ax.grid('on')
    ax.set_xlabel('Names of the class')
plt.show()

