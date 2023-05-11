from numpy import *
from xlrd import open_workbook
import xlrd as xd
import numpy as np
import matplotlib.pyplot as plt
from time import time
import random as rd
from math import exp, sqrt
import itertools


def loadDataSet(fileName):  
    dataMat = []              
    fr = open(fileName,encoding='UTF-8')
    for line in fr.readlines():
        curLine = line.strip().split(' ')
        fltLine = list(map(float, curLine))    
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) 


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    print(n)
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]
    print(m)
    clusterAssment = mat(zeros((m,3)))    
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for index in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[index,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[index,0] != minIndex: clusterChanged = True;  
            np.set_printoptions(suppress=True)
            clusterAssment[index,:] = minIndex,minDist**2,index   
        #print(centroids)
        for cent in range(k):   
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]  
            if len(ptsInClust) > 0:
                centroids[cent,:] = mean(ptsInClust, axis = 0)   
            else:
                centroids[cent,:] = centroids[cent,:]           
    return centroids, clusterAssment


with open("kmeans.txt", "w") as f:
    lines = []
    for index in range(i+1,len(V)):
        lines.append(" ".join([str(V[index][0]), str(V[index][1])])+"\n")
    f.writelines(lines)
datMat = mat(loadDataSet('kmeans2.txt'))
myCentroids,clustAssing = kMeans(datMat,i)
print('The centroids:')
print(myCentroids)
print('The clustering result:')
print(clustAssing)
clustAssing = clustAssing.astype(int)
clust=np.zeros((i,len(V)-1-i))
result=np.matrix(clustAssing)
print(result)

for j  in range(result.shape[0]):
    for index in range(i):
        if result[j,0] == index:
            clust[index,j]=result[j,2]
clust = clust.astype(int)
print(clust)

# The charging time of each outer-ring nodes
tcharge = np.zeros((i,len(V)-1-i))
rset = np.zeros((i,len(V)-1-i))
for j in range(clust.shape[0]):
    for index in range(clust.shape[1]):
        if clust[j,index] != 0:
            a = clust[j,index]
            a = int(a)
            aa = R[a + i] * t / Uc
            aa = round(aa,2)
            rset[j,index] = R[a + i]
            tcharge[j,index] = aa
print('The charging time of each outer-ring nodes:')
print(tcharge)
print(rset)

# The charging time of each outer-ring cluster
TCHARGE = []
for j in range(tcharge.shape[0]):
    tchargemax = [] 
    for index in range(tcharge.shape[1]):
        tchargemax.append(tcharge[j,index])
    TCHARGE.append(max(tchargemax))
print('The charging time of each outer-ring cluster:')
print(TCHARGE)

# The energy consumption rate of each outer-ring cluster
RSET = []
for j in range(rset.shape[0]):
    rouset = [] 
    for index in range(rset.shape[1]):
        rouset.append(rset[j,index])
    RSET.append(max(rouset))
print('The energy consumption rate of the cluster:')
print(RSET)

# The number of the requested nodes for each cluster
Flag = []
for j  in range(clust.shape[0]):
    flag = 0
    for index in range(clust.shape[1]):
        if clust[j,index] > 0:
            flag = flag +1
    Flag.append(flag)








