
import numpy as num
file = file('file.01.p0013.txt','r').readlines()

ListNum = []
for line in file:
	ListNum.append(line.strip('\n'))

NDigit = 50
NNum = 100

sumN = 0
for d in range(49,-1,-1):
	multi = 10**(50-d)
	for n in range(100):
		sumN += int(ListNum[n][d])*multi
	print sumN

print sumN
	
