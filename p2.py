import pandas as pd
import numpy as np

data=pd.DataFrame(data=pd.read_csv("data2.csv"))

concepts=np.array(data.iloc[:,0:-1])
target=np.array(data.iloc[:,-1])
print(concepts)
print(target)

def learn(concepts,targets):
	specific=concepts[0].copy()
	general=[['?' for i in range(len(specific))] for j in range(len(specific))]
	for i,h in enumerate(concepts):
		if target[i]=="Yes":
			for x in range(len(specific)):
				if h[x]!=specific[x]:
					specific[x]='?'
					general[x][x]='?'
		if target[i]=="No":
			for x in range(len(specific)):
				if h[x]!=specific[x]:
					general[x][x]=specific[x]
				else:
					general[x][x]='?'

		print("specific",specific)
		print("general",general)
	ans=[]
	for i,x in enumerate(general):
		if x==["?","?","?","?","?","?"]:
			ans.append(i)
	for i in ans:
		general.remove(["?","?","?","?","?","?"])
	return specific,general

specific,general=learn(concepts,target)
print("final",specific,general)



