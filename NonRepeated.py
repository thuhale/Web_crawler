fi = open('UniqueMakeUp.txt', r)
makeupList = []

for line in fi:
	makeupList.append(line)

makeupList = list(set(makeupList))
print len(makeupList)


	
