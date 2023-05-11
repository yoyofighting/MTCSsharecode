import sys
from xlrd import open_workbook
import xlrd as xd
import pandas as pd
from pylab import *
from time import time


print('Network starts running')

wb = open_workbook('excel1.xlsx')
sheet = wb.sheet_by_name('Sheet1')
initdata = []
for r in range(sheet.nrows):
    data1 = []
    for c in range(sheet.ncols):
        data1.append(sheet.cell_value(r,c))
    initdata.append(list(data1)) 

D = []
V = []
wb = open_workbook('phase_detector.xlsx')
for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        print('the row is:', row)
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(values)
        V.append(values)
        print(V)

        dis = math.sqrt((values[0] - firstPoint[0]) ** 2 + (values[1] - firstPoint[1]) ** 2)
        dis1 = round(dis, 1)
        D.append(dis1)
    D.sort()
    print("The order of the distance between the node and the BS:")
    print(D)
for i in range(len(D) - 1):
    for j in range(len(D) - i - 1):
        if (V[j][0] - V[0][0]) ** 2 + (V[j][1] - V[0][1]) ** 2 > (V[j + 1][0] - V[0][0]) ** 2 + (
                V[j + 1][1] - V[0][1]) ** 2:
            temp = V[j]
            V[j] = V[j + 1]
            V[j + 1] = temp
print("The sorted dataset:")
print(V)

# The number of the inner-ring nodes
total = 0
dis3 = 0
TOTAL=[]
for i in range(len(D) - 1):
    dis2 = math.sqrt((V[i][0] - V[i + 1][0]) ** 2 + (V[i][1] - V[i + 1][1]) ** 2)
    dis3 += dis2
    total = dis3 + math.sqrt((V[i + 1][0] - firstPoint[0]) ** 2 + (V[i + 1][1] - firstPoint[1]) ** 2) 
    TOTAL.append(total)
    if i * Emax + total * Um > Q:
        break
print("The number of the inner-ring nodes:")
print(i)
print("The total moving distance:")
print(TOTAL)    


# The neighbor of the inner-ring nodes
neiset = []
for index in range(i):
    index = index + 1
    b = 0
    for j in range(i):
        j = j + 1
        if j != index and math.sqrt((V[j][0] - V[index][0]) ** 2 + (V[j][1] - V[index][1]) ** 2) < comdis:
            b = b + 1
    neiset.append(b)
print("The neighbor set of inner-ring nodes:")
print(neiset)

# The weight of the neighbor
WSI = []
for index in range(i):
    wsi = (i - neiset[index]) / i
    WSI.append(wsi)
print("The weight of the neighbor:")
print(WSI)







