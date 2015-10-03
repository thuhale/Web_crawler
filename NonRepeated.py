fi = open('SephoraMakeUp.txt', 'r')
fo = open('UniqueMakeUp.txt', 'w+')
makeupList = []

for line in fi:
	makeupList.append(line)
	print line

makeupList = list(set(makeupList))
print len(makeupList)

for item in makeupList:
	fo.write(item)
	
