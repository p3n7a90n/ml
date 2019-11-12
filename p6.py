from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfTransformer,CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report

c=CountVectorizer()

train=fetch_20newsgroups(subset="train",shuffle=True)
print(train.target_names)

categories=["alt.atheism","comp.graphics","sci.med","soc.religion.christian"]
train=fetch_20newsgroups(subset="train",shuffle=True,categories=categories)
print(type(train))
test=fetch_20newsgroups(subset="test",shuffle=True,categories=categories)
tfid=TfidfTransformer()
train_tfid=tfid.fit_transform(c.fit_transform(train.data))
test_tfid=tfid.transform(c.transform(test.data))

model=MultinomialNB()
model.fit(train_tfid,train.target)
predicted=model.predict(test_tfid)


print(confusion_matrix(test.target,predicted))
print(accuracy_score(test.target,predicted))
print(classification_report(test.target,predicted,target_names=test.target_names))