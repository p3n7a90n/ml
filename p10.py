import pandas as pd
import numpy as  np

import matplotlib.pyplot as plt

def kernel(point,xmat,k):
	m,n=np.shape(xmat)
	weights=np.mat(np.eye(m))
	for j in range(m):
		diff=point-X[j]
		weights[j,j]=np.exp(diff*diff.T/(-2.0*k**2))
	return weights
def weighted(point,xmat,ymat,k):
	wei=kernel(point,xmat,k)
	W=((X.T*(wei*X)).I*((X.T)*(wei*ymat.T)))
	return W


def regression(xmat,ymat,k):
	m,n=np.shape(xmat)
	ypred=np.zeros(m)
	for i in range(m):
		ypred[i]=xmat[i]*weighted(xmat[i],xmat,ymat,k)
	return ypred

def plot(X,ypred):
	sortindex=X[:,1].argsort(0)
	print(sortindex)
	xsort=X[sortindex][:,0]
	fig=plt.figure()
	ax=fig.add_subplot(1,1,1)
	ax.scatter(bill,tip,color="green")
	ax.plot(xsort[:,1],ypred[sortindex],color="red")
	plt.xlabel("Bill")
	plt.ylabel("Tip")
	plt.show()


data=pd.read_csv("data10.csv")
bill=np.array(data.total_bill)
tip=np.array(data.tip)

mbill=np.mat(bill)
mtip=np.mat(tip)
m=np.shape(mbill)[1]

one=np.mat(np.ones(m))
print(one.T)
X=np.hstack((one.T,mbill.T))

ypred=regression(X,mtip,0.5)
print(ypred)

plot(X,ypred)





