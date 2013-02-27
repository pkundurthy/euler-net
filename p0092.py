import numpy as np
import itertools as it

def sumDigSq(num):

	numStr = str(num)
	sumSq = np.sum( [x**2 for x in map(int, numStr)] )
	return sumSq

def isSad(num):
	
	Out = False
	while True:
		num = sumDigSq(num)
		if num == 89:
			Out = True
			break
		elif num == 1:
			break
	return Out

def mkSadList(num):

	Dict = {}
	x = 1
	while x < num+1:
		if x == 1:
			Dict[x] = False
			x += 1
		elif x == 89:
			Dict[x] = True
			x += 1
		else:
			k = x
			while True:
				if k == 1:
					Dict[x] = False
					x += 1
					break
				elif k == 89:
					Dict[x] = True
					x += 1
					break
				else:
					k = sumDigSq(k)
	
	return Dict
			
Lim = 10000000
#Lim = 1000
maxSumSq = sumDigSq(Lim-1)
SadDict = mkSadList(maxSumSq)

CountSad = 0
d = 1
while d < Lim:
	sqS = sumDigSq(d)
	if SadDict[sqS]:
		CountSad += 1
	print d, CountSad
	d += 1

print CountSad
		

