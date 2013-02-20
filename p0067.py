
fileObj = open('file.01.p0067.txt','r').readlines()
TList = []
NLev = len(fileObj)

def maxArray(arrT,arrB):
	
	SumList = []
	for j in range(len(arrT)):
		sum1 = arrT[j] + arrB[j]
		sum2 = arrT[j] + arrB[j+1]
		SumList.append(max(sum1,sum2))
	return SumList

for i in range(NLev-2,-1,-1):
	TList_T = map(int, fileObj[i].split())
	TList_B = map(int, fileObj[i+1].split())

	if i == NLev-2:
		SumList = maxArray(TList_T,TList_B)
	else:
		SumList = maxArray(TList_T,SumList)

print SumList

