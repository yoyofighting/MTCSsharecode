from numpy import *
import numpy as np
import random as rd
from math import exp, sqrt
import itertools


vel = []
for j in range(clust.shape[0]):
    velocity = 0
    meanvelocity = 0
    for index in range(clust.shape[1]):
        if clust[j,index] > 0 and Flag[j] > 0:
            velocity += R[clust[j,index] + i]
            meanvelocity = velocity / Flag[j] 
        elif Flag[j] == 0:
            meanvelocity = 0
    vel.append(meanvelocity)
print(vel)

position, velocity = [], []
for index in range(i):
    X1 = myCentroids[index, 0]
    X2 = myCentroids[index, 1]
    position.append([X1, X2])
    velocity.append(vel[index])

A = position[0]
B = position[1]
C = position[2]
D = position[3]
E = position[4]
F = position[5]
G = position[6]
H = position[7]


def getorder(i):
    nodeorder1 = [A,B,C,D,E,F,G,H]
    nodeorder = list(itertools.permutations(nodeorder1,i))
    return nodeorder


def dis(pointA,pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointA[1] - pointB[1]) ** 2)


def sumdis(index, nodeorder,point0):
    sumdis1 = 8*dis(nodeorder[index][0],firstPoint) + 7*dis(nodeorder[index][1],nodeorder[index][0])\
    + 6*dis(nodeorder[index][2],nodeorder[index][1]) + 5*dis(nodeorder[index][3],nodeorder[index][2])\
    + 4*dis(nodeorder[index][4],nodeorder[index][3]) + 3*dis(nodeorder[index][5],nodeorder[index][4])\
    + 2*dis(nodeorder[index][6],nodeorder[index][5]) + 1*dis(nodeorder[index][7],nodeorder[index][6])
    return sumdis1


def gettime(TCHARGE,i):
    TCHARGE = list(itertools.permutations(TCHARGE,i))
    return TCHARGE


def sumtime(index,TCHARGE):
    sumtime1 = 8*TCHARGE[index][0] + 7*TCHARGE[index][1] + 6*TCHARGE[index][2] + 5*TCHARGE[index][3]\
        + 4*TCHARGE[index][4] + 3*TCHARGE[index][5] + 2*TCHARGE[index][6] + 1*TCHARGE[index][7]
    return sumtime1


def objFuntion(a, b, Vm):
    fit = a / Vm + b
    return fit


def calculateMass(fitness):
    mass = []
    Mass = []
    if min(fitness) != max(fitness):
        for i in range(len(fitness)):
            mass.append((fitness[i] - max(fitness)) / (min(fitness) - max(fitness)))
        for i in range(len(mass)):
            Mass.append(mass[i] / sum(mass))
    else:
        for i in range(len(fitness)):
            Mass.append(1)
    return Mass


def findTopK(fitness, K):
    topK = []
    dic = {}
    for i in range(len(fitness)):
        dic[i] = fitness[i]
    fitness.sort()
    for i in range(K):
        topK.append(list(dic.keys())[list(dic.values()).index(fitness[i])])
    return topK


def calculateAcceleration(nodeorder, Mass, G, topK):
    acceleration = []
    Fi0, Fi1, Fi2, Fi3, Fi4, Fi5, Fi6, Fi7 = 0, 0, 0, 0, 0, 0, 0, 0 

    for i in range(len(nodeorder)):
        for j in range(len(nodeorder)):
            if i != j and j in topK:
                Fi0 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][0],nodeorder[i][0]))
                Fi1 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][1],nodeorder[i][1]))
                Fi2 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][2],nodeorder[i][2]))
                Fi3 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][3],nodeorder[i][3]))
                Fi4 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][4],nodeorder[i][4]))
                Fi5 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][5],nodeorder[i][5]))
                Fi6 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][6],nodeorder[i][6]))
                Fi7 += rd.random() * G1 * ((Mass[i] * Mass[j]) / (calculateDistance(nodeorder[i], nodeorder[j]) + r)) * (
                            dis(nodeorder[j][7],nodeorder[i][7]))
            
                
        if Mass[i] != 0:
            acceleration.append([Fi0 / Mass[i] / 10, Fi1 / Mass[i] / 10, Fi2 / Mass[i] / 10, Fi3 / Mass[i] / 10, 
            Fi4 / Mass[i] / 10, Fi5 / Mass[i] / 10, Fi6 / Mass[i] / 10, Fi7 / Mass[i] / 10])   #这里除10是为了避免粒子的加速度过大
        else:
            acceleration.append([10, 10, 10, 10, 10, 10, 10, 10])
        Fi0 = 0
        Fi1 = 0
        Fi2 = 0
        Fi3 = 0
        Fi4 = 0
        Fi5 = 0
        Fi6 = 0
        Fi7 = 0
    return acceleration


def updateVelocityAndPosition(acceleration, nodeorder, velocity):
    for i in range(len(velocity)):
        velocity[i] = rd.random() * velocity[i] + max(acceleration[i])
        nodeorder[i][0][0] = nodeorder[i][0][0] + velocity[i]
        nodeorder[i][0][1] = nodeorder[i][0][1] + velocity[i]
        nodeorder[i][1][0] = nodeorder[i][1][0] + velocity[i]
        nodeorder[i][1][1] = nodeorder[i][1][1] + velocity[i]
        nodeorder[i][2][0] = nodeorder[i][2][0] + velocity[i]
        nodeorder[i][2][1] = nodeorder[i][2][1] + velocity[i]
        nodeorder[i][3][0] = nodeorder[i][3][0] + velocity[i]
        nodeorder[i][3][1] = nodeorder[i][3][1] + velocity[i]
        nodeorder[i][4][0] = nodeorder[i][4][0] + velocity[i]
        nodeorder[i][4][1] = nodeorder[i][4][1] + velocity[i]
        nodeorder[i][5][0] = nodeorder[i][5][0] + velocity[i]
        nodeorder[i][5][1] = nodeorder[i][5][1] + velocity[i]
        nodeorder[i][6][0] = nodeorder[i][6][0] + velocity[i]
        nodeorder[i][6][1] = nodeorder[i][6][1] + velocity[i]
        nodeorder[i][7][0] = nodeorder[i][7][0] + velocity[i]
        nodeorder[i][7][1] = nodeorder[i][7][1] + velocity[i]

def calculateDistance(p1,p2):
    return dis(p1[0],p2[0]) + dis(p1[1],p2[1]) + dis(p1[2],p2[2]) + dis(p1[3],p2[3]) 
    + dis(p1[4],p2[4]) + dis(p1[5],p2[5]) + dis(p1[6],p2[6]) + dis(p1[7],p2[7]) 

def checkPosition(nodeorder):
    for i in range(len(nodeorder)):
        if nodeorder[i][0][0] < 0:
            nodeorder[i][0][0] = 0
        elif nodeorder[i][0][0] > 2 * L:
            nodeorder[i][0][0] = 2 * L
        if nodeorder[i][0][1] < 0:
            nodeorder[i][0][1] = 0
        elif nodeorder[i][0][1] > 2 * L:
            nodeorder[i][0][1] = 2 * L

        if nodeorder[i][1][0] < 0:
            nodeorder[i][1][0] = 0
        elif nodeorder[i][1][0] > 2 * L:
            nodeorder[i][1][0] = 2 * L
        if nodeorder[i][1][1] < 0:
            nodeorder[i][1][1] = 0
        elif nodeorder[i][1][1] > 2 * L:
            nodeorder[i][1][1] = 2 * L

        if nodeorder[i][2][0] < 0:
            nodeorder[i][2][0] = 0
        elif nodeorder[i][2][0] > 2 * L:
            nodeorder[i][2][0] = 2 * L
        if nodeorder[i][2][1] < 0:
            nodeorder[i][2][1] = 0
        elif nodeorder[i][2][1] > 2 * L:
            nodeorder[i][2][1] = 2 * L

        if nodeorder[i][3][0] < 0:
            nodeorder[i][3][0] = 0
        elif nodeorder[i][3][0] > 2 * L:
            nodeorder[i][3][0] = 2 * L
        if nodeorder[i][3][1] < 0:
            nodeorder[i][3][1] = 0
        elif nodeorder[i][3][1] > 2 * L:
            nodeorder[i][3][1] = 2 * L

        if nodeorder[i][4][0] < 0:
            nodeorder[i][4][0] = 0
        elif nodeorder[i][4][0] > 2 * L:
            nodeorder[i][4][0] = 2 * L
        if nodeorder[i][4][1] < 0:
            nodeorder[i][4][1] = 0
        elif nodeorder[i][4][1] > 2 * L:
            nodeorder[i][4][1] = 2 * L

        if nodeorder[i][5][0] < 0:
            nodeorder[i][5][0] = 0
        elif nodeorder[i][5][0] > 2 * L:
            nodeorder[i][5][0] = 2 * L
        if nodeorder[i][5][1] < 0:
            nodeorder[i][5][1] = 0
        elif nodeorder[i][5][1] > 2 * L:
            nodeorder[i][5][1] = 2 * L

        if nodeorder[i][6][0] < 0:
            nodeorder[i][6][0] = 0
        elif nodeorder[i][6][0] > 2 * L:
            nodeorder[i][6][0] = 2 * L
        if nodeorder[i][6][1] < 0:
            nodeorder[i][6][1] = 0
        elif nodeorder[i][6][1] > 2 * L:
            nodeorder[i][6][1] = 2 * L

        if nodeorder[i][7][0] < 0:
            nodeorder[i][7][0] = 0
        elif nodeorder[i][7][0] > 2 * L:
            nodeorder[i][7][0] = 2 * L
        if nodeorder[i][7][1] < 0:
            nodeorder[i][7][1] = 0
        elif nodeorder[i][7][1] > 2 * L:
            nodeorder[i][7][1] = 2 * L


minfitness = []
bestorder = []
fitness = []
nodeorder = getorder(i)
tcharge2 = gettime(TCHARGE,i)
# The fitness
for index in range(len(nodeorder)):
    totaldis = sumdis(index, nodeorder, firstPoint) 
    totaltime = sumtime(index,tcharge2)
    fit = objFuntion(totaldis, totaltime,Vm)
    fitness.append(fit)

# Update the gravity constant
G1 = G1 * exp(-20 * iterx / maxIterx)

# Update the mass of the object
Mass = calculateMass(fitness) 

# Find the top K object
topK = findTopK(fitness, K)

# The acceleration of the object
acceleration = calculateAcceleration(nodeorder, Mass, G1, topK) 

# Update the velocity and position of the object
updateVelocityAndPosition(acceleration, nodeorder, velocity)

# Check if the object is out of space
checkPosition(nodeorder)

# Update the K
K = K - iterx
minfitness.append(min(fitness))
bestorder.append(nodeorder[fitness.index(min(fitness))])
print(bestorder)
print(minfitness)

# The average task delay in the outer ring
print("The average task delay in the outer ring:")
print((min(minfitness))/(len(V) - 1 - i))


# The energy efficiency of the outer ring
for index in range(i-1):
    outdis = dis(bestorder[-1][index],bestorder[-1][index+1])
totaloutdis = dis(firstPoint,bestorder[-1][0]) + outdis + dis(firstPoint,bestorder[-1][-1])
outeita = (sum(TCHARGE) * Uc) / (sum(TCHARGE) * Uc + totaloutdis * Um)
print("The energy efficiency of the outer ring:: ", outeita) 

# The charging failure rate of the outer ring
waitdis = []
waitdis.append(0)
waitcha = []
waitcha.append(0)
nodeorder1 = [A,B,C,D,E,F,G,H]
waitsumdis = 0
waitsumchar = 0 
for index in range(len(bestorder[0])-1):
    betweendis = dis(bestorder[0][index],bestorder[0][index+1])
    waitsumdis = waitsumdis + betweendis
    waitdis.append(waitsumdis)
for index in range(len(TCHARGE)-1):
    waitsumchar = waitsumchar + TCHARGE[nodeorder1.index(bestorder[0][index])]
    waitcha.append(waitsumchar)
print('The waiting time:')
print(waitcha)

odead = 0
for j in range(len(clust)):
    for index in clust[j]:
        if index != 0:
            if Emax - (waitdis[j] / Vm + waitcha[j]) * R[index + i] < Emin:
                odead = odead + 1
        else:
            odead = odead
print("The charging failure rate of the outer ring:")
odeadrate = odead / (len(V) - i)
print(odeadrate)

