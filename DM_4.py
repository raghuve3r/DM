__author__ = 'raghuveer'
import math
import numpy
import random
from collections import defaultdict
from matplotlib import pyplot
from scipy.spatial.distance import pdist,squareform

print "Question 4"

#Initialization of variables
datamx = []
K_for_Xaxis =[]
RK_for_YAxis = []
listoflists = []
a_list = []

#Graph plotting. Using functions of Matplotlib.

for k in range(0,100):
    one_dimension =[]
    for n in range(0,100): # The value can be 100,1000 or 10000
            a_list = (list([random.uniform(0,1) for i in range(k+1)]))
            one_dimension.append(a_list)
    one_dimension = numpy.array(one_dimension)    #Convertion of array into single dimension.
    #printing single dimension list
    datamx = pdist(one_dimension,'Euclidean')
    #print squareform(datamatrix)
    max_dist = numpy.max(datamx)
    #print max_dist
    min_dist = numpy.min(datamx[numpy.nonzero(datamx)]) #non zero matrix
    #print min_dist
    RK_for_YAxis.append(math.log((max_dist-min_dist)/min_dist,10))
    K_for_Xaxis.append(k+1)


pyplot.xlabel('k')
pyplot.ylabel('R(k)')
pyplot.title('Plot of R(k) against k:The curse of Dimensionality')
pyplot.legend()
pyplot.plot(K_for_Xaxis, RK_for_YAxis, linestyle='-', color='g')
pyplot.legend()
pyplot.show()

