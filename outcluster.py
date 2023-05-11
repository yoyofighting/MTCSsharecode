import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from xlrd import open_workbook
import xlrd as xd
from pylab import *


centers = []
for index in range(i):
    index = index + 1
    C = (V[index][0] , V[index][1])
    centers.append(C)
print(centers)

datas=[]
V = np.array(V)
for clusterdata in V[i+1:,0:2]:
    datas.append(clusterdata)
datas = np.array(datas)
data=datas.astype(np.float)
print(data)

def plot_clustering(X, labels, title=None):
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='coolwarm')
    if title is not None:
        plt.title(title, size=17)
    plt.axis('off')
    plt.tight_layout()


plt.scatter(x=data[:, 0:1], y=data[:, 1:2], marker='.', color='red')
n = np.arange(data.shape[0])
for index, txt in enumerate(n):
    plt.annotate(txt, (data[index:index + 1, 0:1], data[index:index + 1, 1:2]))
plt.show()


ac = AgglomerativeClustering(n_clusters = i, affinity='euclidean', linkage='average')
clustering = ac.fit(data)

print("Each data belongs to the serial number of the cluster:", clustering.labels_)
print("The member of each cluster:", clustering.children_)

Z = linkage(data, 'average')
print("The process of clustering:", Z)

f = fcluster(Z, i, 'maxclust')
print("The clustering results:", f)
fig = plt.figure(figsize=(5, 3))
dn = dendrogram(Z)
plt.show()

plot_clustering(data, f, '%s linkage')
plt.show()
