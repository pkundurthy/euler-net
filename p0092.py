import numpy as np

def sumDigSq(num):

	numStr = str(num)
	sumSq = np.sum( [x**2 for x in map(int, numStr)] )
	return sumSq

Count89 = 0
MaxL = 1001
MaxL = 10000001
x = 1
while x < MaxL:
	k = x
	Cycle = 0
	while k not in [1,89]:
		k = sumDigSq(k)
		Cycle += 1

	if k == 89:
		print x, Cycle
		Count89 += 1

	x += 1

print Count89
"""
for x in xrange(1,MaxL,1):
	k = x
	while k not in [1,89]:
		k = sumDigSq(k)

	if k == 89:
		print x
		Count89 += 1



"""
