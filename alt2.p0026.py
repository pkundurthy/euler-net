
# Code stolen from Rosetta code for multiplicative order

import numpy as np

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def lcm(a, b):
    return (a*b) / gcd(a, b)
 
def isPrime(p):
    return (p > 1) and all(f == p for f,e in factored(p))
 
primeList = [2,3,5,7]
def primes():
    for p in primeList:
        yield p
    while 1:
        p += 2
        while not isPrime(p):
            p += 2
        primeList.append(p)
        yield p
 
def factored( a):
    for p in primes():
        j = 0
        while a%p == 0:
            a /= p
            j += 1
        if j > 0:
            yield (p,j)
        if a < p*p: break
    if a > 1:
        yield (a,1)
 
def multOrdr1(a,(p,e) ):
    m = p**e
    t = (p-1)*(p**(e-1)) #  = Phi(p**e) where p prime
    qs = [1,]
    for f in factored(t):
        qs = [ q * f[0]**j for j in range(1+f[1]) for q in qs ]
    qs.sort()
 
    for q in qs:
        if pow( a, q, m )==1: break
    return q
 
 
def multOrder(a,m):
    assert gcd(a,m) == 1
    mofs = (multOrdr1(a,r) for r in factored(m))
    return reduce(lcm, mofs, 1)


Nmax = 0
MaxNum = 0

for x in range(1,1001,1):
	if gcd(10,x) != 1:
		x0 = x
		while gcd(10,x) != 1:
			x = x/gcd(10,x)
		if x == 1:
			mo = 0
		else:
			mo = multOrder(10,x)
		Np = mo
		num = x0
	else:
	 	Np = multOrder(10,x)
		num = x
	if Np > Nmax:
		Nmax = Np
		MaxNum = num

print Nmax
print MaxNum

"""
	if (x%2 == 0 and x%5 == 0) or isPower2(x) or isPower5(x):
		print '0', x
	else:
		print multOrder(10,x), x
"""



