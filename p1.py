import csv
reader=csv.reader(open("data1.csv"))
data=[]
for i in reader:
	if i[-1]=="yes":
		data.append(i)

rows=len(data)
column=len(data[0])-1

hypo=['%' for i in range(column)]

print(hypo)

hypo=data[0][:-1]

for i in range(rows):
	for j in range(column):
		if hypo[j]!=data[i][j]:
			hypo[j]='?'
print("final",hypo)