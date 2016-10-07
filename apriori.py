from collections import defaultdict
def extractData(fileName):
    #print("extracting file")
    file = open(fileName, 'r')
    columnDict={}
    #transDetails={}
    columnCount=0;
    transCount=0;
    transDetails = defaultdict(list)

    print ("Filepath is:" + file.name)
    for everyLine in file:
        values=everyLine.strip().split(",")
        for value in values:
            transDetails[transCount].append(value)
            if value not in columnDict.values():
                columnDict[columnCount]=value
                columnCount+=1
        transCount += 1;

    print columnDict
    print transDetails
    print transCount
    print columnCount
    transMatrix = [[0 for i in range(columnCount-1)] for j in range(transCount-1)]


    for row in range(transCount-1):
        for column in range(columnCount-1):
            for k,v in transDetails.iteritems():
                if k==row:
                    if columnDict.get(column) in v:
                        #print "columnDict.get(column) is", columnDict.get(column)
                        #print "v is", v
                        #print row
                        #print column
                        transMatrix[row][column]=1
    return columnDict, transCount, columnCount, transDetails,transMatrix


def genFrequent(columnDict,supportCount,transDetails):
    candSupportDict={}
    itemSet = set()
    for candidate in columnDict:
        candidateCount = 0.0
        for k,v in transDetails.iteritems():
            if columnDict.get(candidate) in v:
                candidateCount+=1
                candidateSupportCount=float(candidateCount/len(transDetails))
                #print "candidateSupportCount",candidateSupportCount
                if candidateSupportCount>supportCount:
                    candSupportDict[columnDict.get(candidate)] = candidateSupportCount
                    itemSet.add(frozenset([columnDict.get(candidate)]))
    return candSupportDict,itemSet


def genFrequent1(columnDict,supportCount,transDetails):
    candSupportDict={}
    itemSet = set()
    #print columnDict
    for candidate in columnDict:
        #print candidate
        candidateCount = 0.0
        for k,v in transDetails.iteritems():
            if candidate.issubset(v):
                candidateCount+=1
                candidateSupportCount = float(candidateCount / len(transDetails))
                #print "candidateSupportCount",candidateSupportCount
                if candidateSupportCount>supportCount:
                    candSupportDict[candidate] = candidateSupportCount
                    itemSet.add(frozenset(candidate))
    return candSupportDict,itemSet

def candidate_gen(freq_sets, k):
    """Join a set with itself and returns the n-element itemsets"""
    returnSet = set()
    for i in freq_sets:
        for j in freq_sets:
            if len(i.union(j))==k:
                returnSet.update(set([i.union(j)]))
    return returnSet



    #return [i.union(j) for i in freq_sets for j in freq_sets if len(i.union(j)) == k]


def Apriori(columnDict,supportCount,transDetails):
    k=1
    #frequentlstList=[]
    #frequentList={}
    frequentList,itemSet=genFrequent(columnDict,supportCount,transDetails)
    print "freq list is",frequentList
    print "itemset is",itemSet
    #frequentlstList = [ k for k in frequentList]
    #frequentlstList=frequentlstList.ToList()
    #print "candidate-1 item list is", frequentlstList
    #k=2
    #while(itemSet != set([])):
    while(itemSet):
        k+=1
        frequentList=candidate_gen(itemSet,k)
        #print frequentList
        frequentList, itemSet = genFrequent1(frequentList, supportCount, transDetails)
        if(itemSet == set([])):
            break
        print "freq list is", frequentList
        print "itemset is", itemSet





#main

fileName="data2.txt"
supportCount=0.1
columnDict,transCount,columnCount,transDetails,transMatrix=extractData(fileName)
Apriori(columnDict,supportCount,transDetails)
#print transMatrix

