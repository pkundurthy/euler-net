

def numfac(num):
	div = 1
	fac0 = []
	fac1 = [num]
	while div < min(fac1): 
		#print fac0, fac1
		if num%div == 0:
			fac0.append(div)
			fac1.append(num/div)
	
		div += 1

	return len(fac0)+len(fac1)-1


t = 1
ndiv = 1
ndiv_max = 501
tnum = 1
while ndiv < ndiv_max:
	t += 1
	tnum += t
	ndiv = numfac(tnum)
	print t, tnum, ndiv

print t, tnum, ndiv



