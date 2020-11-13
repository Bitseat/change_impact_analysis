import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle


model_test = pickle.load(open("clustering_model.pkl", "rb"))


test = pd.read_csv("testing.csv",header = None)

origin = pd.read_csv("req_vecs.csv", header = None)
origin_data = pd.read_csv("all_requirements.csv")
new = origin.append(test) 
new.to_csv("newone.csv")
New = StandardScaler().fit_transform(new)


pred = model_test.fit_predict(New)


size = len(pred) -1
d = pred[size]
#print(d) 

candidates = []
for i in range(0, len(pred)):
    if pred[i] == d:
        candidates.append(i)

print(candidates)
i = 0
for index, row in origin_data.iterrows():
    for x in candidates:
        if index == x and i < 5:
            print(row['Issue_key'])
            i = i + 1

#print(type(pred))


