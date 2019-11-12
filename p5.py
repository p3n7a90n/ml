from csv import reader
from random import seed,shuffle
from math import exp,pi,sqrt
from operator import itemgetter

import numpy as np
seed(2)

data=np.array(list(reader(open("data5.csv"))),dtype="float")
shuffle(data)

trainlen=int(0.9*len(data))

traindata,traintarget=data[:trainlen,:-1],data[:trainlen,-1]
testdata,testtarget=data[trainlen:,:-1],data[trainlen:,-1]

def safedic(x,y):
	return x/y if y!=0 else 0
def prob(x,mean,std):
	temp=exp(-((x-mean)**2/2*std**2))
	return safedic(1,sqrt(2*pi*std*std))*temp

classses={}
for attrs,target in zip(traindata,traintarget):
 	if target not in classses:
 		classses[target]=[]
 	classses[target].append(attrs)

summaries={}

for cls in classses.keys():

 	summaries[cls]=[]
 	for column in zip(*classses[cls]):
 		summaries[cls].append((np.mean(column),np.std(column)))
correct=0
for attrs,target in zip(testdata,testtarget):
	probab={}
	for cls in classses.keys():
		probab[cls]=1
		for i,(mean,std) in enumerate(summaries[cls]):
			probab[cls]*=prob(attrs[i],mean,std)
	cls=sorted(probab.items(),key=itemgetter(1),reverse=True)[0][0]

	print("actual",target)
	print("predicted",cls)
	if cls==target:
		correct+=1
print("accuracy",correct/len(testdata))

