#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:29:00 2018

@author: chidanandapati, Himangini Agrawal, Vidhi Sharma
"""

import numpy as np
import pandas as pd  
from sklearn.cluster import KMeans as km
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')

#Read csv file
data = pd.io.parsers.read_csv(r'/Users/himangini/Desktop/CMPE-257/Assignment1/movie_metadata.csv',error_bad_lines=False)
print ("This is the shape of my data")
print (data.shape)

#drop rows with missing values
data.dropna(inplace=True)
data.head()

#plotting values
f1 = data['duration'].values
f2 = data['imdb_score'].values
X = np.array(list(zip(f1, f2)))
print ("This is X. The zipped array")
print (X)

#Finding optimal k
wcss = []

for i in range(1, 11):
    kmeans = km(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
#Plotting the results onto a line graph, allowing us to observe 'The elbow'
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') #within cluster sum of squares
plt.show()


k=4
kmeans=km(n_clusters=k)
KMmodel=kmeans.fit(X)
labels=KMmodel.labels_
centroids=KMmodel.cluster_centers_
print("centroids")
print(centroids)

#data points for each cluster
#{i: X[np.where(KMmodel.labels_ == i)] for i in range(KMmodel.n_clusters) }

def ClusterIndicesNumpy(clustNum, labels_array): #numpy 
    return np.where(labels_array == clustNum)[0]

print ("data points for cluster 0 are -")
print (X[ClusterIndicesNumpy(0, KMmodel.labels_)])

print ("data points for cluster 1 are -")
print (X[ClusterIndicesNumpy(1, KMmodel.labels_)])

print ("data points for cluster 2 are -")
print (X[ClusterIndicesNumpy(2, KMmodel.labels_)])

print ("data points for cluster 3 are -")
print (X[ClusterIndicesNumpy(3, KMmodel.labels_)])

print ("data points for cluster 4 are -")
print (X[ClusterIndicesNumpy(4, KMmodel.labels_)])

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()

for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if labels[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')


