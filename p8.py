from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
colormap = np.array(['red', 'lime', 'black'])
data=load_iris()
#data=pd.DataFrame(pd.read_csv("data8.csv"))

#print(data)
X,Y=data.data,data.target
#print(X,Y)

Kmeans=KMeans(n_clusters=3)
Kmeans.fit(X)

gauss=GaussianMixture(n_components=3)
gauss.fit(X)
predict=gauss.predict(X)

print("Kmeans",silhouette_score(X,Kmeans.labels_))
print("GaussianMixture",silhouette_score(X,predict))

def plot(i,title,target):
	plt.subplot(2,2,i)
	plt.scatter(X[:, 2],X[:, 3],c=colormap[target])
	plt.title(title)
	plt.xlabel("Petal lenght")
	plt.ylabel("Petal width")


plot(1,"real",Y)
plot(2,"Kmeans",Kmeans.labels_)

plot(3,"real",Y)

plot(4,"Kmeans",predict)

plt.show()


