__author__ = 'raghuveer'


import csv
import numpy
import math
from random import randint
import collections
from scipy.spatial.distance import pdist, squareform

#initializing the file
userListMovies = []
userListMoviesTest = []
userId = []
movieId = []

#user count and movie count info got from the u.info file
userCount = 8
movieCount = 7

#reading the file of user,movie and ratings
with open('dm_test.data', 'r') as f:
    userList = csv.reader(f, delimiter='\t')
    for row in userList:
        row = map(int,row)
        userListMovies.append(row)
f.close()

#initializing dictionaries

userListDict = {}
similarUserDict = {}
userNotSeenDict = {}
userTestDict = {}

for x in userListMovies:
    userListDict.update({(x[0],x[1]):x[2]})

#user table initialization having user id and movie id
user_table = [[0 for i in range(movieCount)] for j in range(userCount)]

#filling  the user table with value read from the file
for x in userListMovies:
    user_table[x[0]-1][x[1]-1] = userListDict[x[0],x[1]]

#table to fill Lmax distance between the users
lm_distance_table = [[0 for i in range(userCount)] for j in range(userCount)]

#filling the Lmax distance table between users
for x in range(userCount):
    for y in range(userCount):
        if x != y:
            num_array = numpy.array([user_table[x],numpy.array(user_table[y])])
            lm_distance_table[x][y] = float(str(pdist(num_array ,'chebyshev')).replace('[','').replace(']',''))

#finding the similar users for a particular user
for x in range(userCount):
    for y in range(userCount):
        if lm_distance_table[x][y] > 0.1 and lm_distance_table[x][y] < 2.0:
            if x+1 not in similarUserDict:
                similarUserDict[x+1] = [y + 1]
            else:
                similarUserDict[x+1].append(y+1)

#check user table to see if a user has seen a movie or not.
# If he has not seen, check if he has similar users and then infer the rating for the user from the ratings on the movie by the similar users.
# If no similar users then average the rating of all the users who have seen the movie
for x in range(userCount):
    for y in range(movieCount):
        if user_table[x][y] == 0:
            if x+1 in similarUserDict:
                aggregate_1 = []
                aggregate_2 = []
                k = 4
                similar_list = []
                lmList = {}
                similar_list = similarUserDict[x+1]
                for i in similar_list:
                    lmList.update({lm_distance_table[x][i-1]:i})
                lmDict = {}
                lmDict = collections.OrderedDict(sorted(lmList.items(), key=lambda t: t[0]))
                for z in range(k):
                    rating = lmDict.itervalues().next()
                    aggregate_1.append(rating)
                userNotSeenDict.update({(x+1,y+1):sum(aggregate_1)/len(aggregate_1)})
            else:
                aggregate_3 = []
                for i in range(userCount):
                    if user_table[i][y] != 0:
                        aggregate_3.append(user_table[i][y])
                if len(aggregate_3) != 0:
                    userNotSeenDict.update({(x+1,y+1):sum(aggregate_3)/len(aggregate_3)})
                else:
                    userNotSeenDict.update({(x+1,y+1):3})


#reading the test data
with open('dm_train.data', 'r') as f1:
    userListTest = csv.reader(f1, delimiter='\t')
    for row in userListTest:
        row = map(int,row)
        userListMoviesTest.append(row)
f.close()

#creating a dictionary from the test data
for x in userListMoviesTest:
    userTestDict.update({(x[0],x[1]):x[2]})




MAD = []
r_ij = 0
p_ij = 0
t_ij = 0

#calculation of MAD
for key in userTestDict:
    r_ij = r_ij + 1
    p_ij = userNotSeenDict[key]
    t_ij = userTestDict[key]
    MAD.append(abs(p_ij - t_ij))

mad = sum(MAD)
rij=r_ij
Lm_MAD = 0
Lm_MAD = mad / (rij * 1.0)
print Lm_MAD