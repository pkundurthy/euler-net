import numpy as np


def getDivisors(Number):

	ListDiv = [1]
	fac = 2
	while fac <= float(Number)/2.0:
		if Number % fac == 0:
			ListDiv.append(fac)
		fac += 1

	Sum = np.sum(ListDiv)
	return ListDiv, Sum


amicable = []
a = 0
while a < 10000:
	
	DivList1, Sum_a = getDivisors(a)
	DivList2, Sum_b = getDivisors(Sum_a)
	if Sum_b == a and a != Sum_a:
		amicable.append(a)
		amicable.append(Sum_a)
		print a

	a += 1

print amicable
print np.sum(list(set(amicable)))

