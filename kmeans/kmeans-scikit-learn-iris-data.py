#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 20:29:00 2018

@author: chidanandapati, Himangini Agrawal, Vidhi Sharma
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans as km
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


#Loda iris data
#http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
iris = load_iris()

X = iris.data

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


k=3
kmeans=km(n_clusters=k)
KMmodel=kmeans.fit(iris.data)
labels=KMmodel.labels_
centroids=KMmodel.cluster_centers_
print("centroids")
print(centroids)

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()

for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if labels[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')


