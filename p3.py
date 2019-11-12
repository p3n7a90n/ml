import pandas as pd
from math import log
class Node:
	def __init__(self,l):
		self.label=l
		self.branches={}

def entropy(data):
	total_len=len(data)
	positive_example=len(data.loc[data["PlayTennis"]=="Y"])
	#print(positive_example)
	#print(data.columns)
	#print(positive_example)
	negative_example=len(data.loc[data["PlayTennis"]=="N"])
	entropy=0
	if positive_example>0:
		entropy=-1*((positive_example/float(total_len))*log(positive_example,2)-log(total_len,2))
	if negative_example>0:
		entropy+=-1*((negative_example/float(total_len))*log(negative_example,2)-log(total_len,2))
	return entropy

def gain(s,attr,data):
	values=set(data[attr])
	print(values)
	gain=s
	for val in values:
		gain-=(len(data.loc[data[attr]==val])/float(len(data))*entropy(data.loc[data[attr]==val]))
	return gain
def getattrib(data):
	entropy_s=entropy(data)
	attribute=""
	maxgain=0
	#print("list",data.columns[:len(data.columns)-1])
	for attr in data.columns[:-1]:
		#print("test",attr)

		g=gain(entropy_s,attr,data)
		if g>maxgain:
			maxgain=g
			attribute=attr
	return attribute

	
def tree(data):
	root=Node("NULL")
	if entropy(data)==0:
		if len(data.loc[data[data.columns[-1]]=="Y"])==len(data):
			root.label="Y"
			return root
		else:
			root.label="N"
			return root
	if (len(data.columns)==1):
		return
	else:
		attrib=getattrib(data)
		root.label=attrib
		values=set(data[attrib])
		for val in values:
			root.branches[val]=tree(data.loc[data[attrib]==val].drop(attrib,axis=1))
	return root


def get_rules(root,rule,rules):
	if not root.branches:
		rules.append(rule[:-2]+" => "+root.label)
		return rules
	for i in root.branches:
		get_rules(root.branches[i],rule+root.label+"="+i+" ^ ",rules)
	return rules
def test(tree,test_str):
	if not tree.branches:
		return tree.label
	return test(tree.branches[test_str[tree.label]],test_str)

data=pd.read_csv("data3.csv")
#entropy_s=entropy(data)

#print("test",data.columns)
tree=tree(data)



rules=get_rules(tree,"",[])
print(rules)

test_str={}
print("test data>:")
for i in data.columns[:-1]:
	test_str[i]=input(i+": ")

print(test_str)
print(test(tree,test_str))
