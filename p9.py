from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

import numpy as np

data=load_iris()
print(data.target_names)
print(data["data"])
X_train,X_test,Y_train,Y_test=train_test_split(data["data"],data["target"])

classifier=KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train,Y_train)
ypred=classifier.predict(X_test)

for i in range(len(ypred)):
	print("Training example")
	print(X_test[i])
	print("Actual label")
	print(Y_test[i])
	print("predict")
	print(ypred[i])

print(confusion_matrix(Y_test,ypred))

print(classification_report(Y_test,ypred,target_names=data.target_names))
