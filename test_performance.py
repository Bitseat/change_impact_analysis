import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn import metrics

model_test = pickle.load(open("clustering_model.pkl", "rb"))

New = pd.read_csv("performance_testing.csv",header = None)

labels_pred = model_test.fit_predict(New)

#print(labels_pred)
labels_true = [1,1,4,3,3,1,4,5,6,6,6,7,6,7,7,1,4,5,2,2]
#labels_true = [1,1,2,7,0,3,0,5,0,2,0,0,2,2,2,6,4,0,0,2]

accuracy2 = metrics.mutual_info_score(labels_true, labels_pred)

accuracy3 = metrics.normalized_mutual_info_score(labels_true, labels_pred) 
accuracy = metrics.adjusted_mutual_info_score(labels_true, labels_pred)  

accuracy4 = metrics.adjusted_rand_score(labels_true, labels_pred)

homogeneity = metrics.homogeneity_score(labels_true, labels_pred)

completeness = metrics.completeness_score(labels_true, labels_pred)

vmeasure = metrics.v_measure_score(labels_true, labels_pred, beta=0.6)
fowlkes = metrics.fowlkes_mallows_score(labels_true, labels_pred)
hcv = metrics.homogeneity_completeness_v_measure(labels_true, labels_pred)
print("mutual_info_score", accuracy3)

#print(fowlkes)
print("homogeneity, completeness, v_measure scores are", hcv)







