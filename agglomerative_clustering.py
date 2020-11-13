import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle
#%matplotlib inline

from sklearn.datasets import make_blobs


df = pd.read_csv("input.csv", header = None)
col_size = df.shape[1]

df.columns = ['vec'+str(x) for x in range(0,col_size)]
df = df.applymap('{:.6f}'.format)

df.to_csv("input_with_index.csv", header = True, index = True)

x = pd.read_csv("input_with_index.csv")

X = StandardScaler().fit_transform(x)

new_row_size = X.shape[0]
#new_row_size = row_size + 13*n
print(new_row_size)
n = round((new_row_size - 100 )/13)

initial_clusters = 7
n_clusters = initial_clusters

if n == 0:
        n_clusters = n_clusters
else:

    for l in range(1,10000):
    
        if n == l:
            n_clusters = initial_clusters + l
        else:
            n_clusters = n_clusters

print(n_clusters)

# import hierarchical clustering libraries
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from array import *


# create dendrogram
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))
# create clusters
hc = AgglomerativeClustering(n_clusters=n_clusters, affinity = 'euclidean', linkage = 'ward')
# save clusters for chart
y_hc = hc.fit_predict(X)

print(y_hc)
plt.scatter(X[y_hc ==0,0], X[y_hc == 0,1], s=100, c='red')
plt.scatter(X[y_hc==1,0], X[y_hc == 1,1], s=100, c='black')
plt.scatter(X[y_hc ==2,0], X[y_hc == 2,1], s=100, c='blue')
plt.scatter(X[y_hc ==3,0], X[y_hc == 3,1], s=100, c='cyan')
plt.scatter(X[y_hc ==4,0], X[y_hc == 4,1], s=100, c='yellow')
plt.scatter(X[y_hc ==5,0], X[y_hc == 5,1], s=100, c='green')
plt.scatter(X[y_hc ==6,0], X[y_hc == 6,1], s=100, c='orange')


pickle.dump(hc, open("clustering_model.pkl", "wb"))





