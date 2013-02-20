
import sys

def isPrime(number):

	Out = True
	if number%2 == 0:
		Out = False
	elif number < 0:
		Out = False
	else:
		fac = 3
		while fac <= number/2:
			if number%fac == 0:
				Out = False
				break
			else:
				fac += 2
			
	return Out

MaxLN = 0
maxA = 0
maxB = 0

for a in range(-1000,1001,1):
	for b in range(-1000,1001,1):
#for a in [1,-79]:
#	for b in [41,1601]:
		checkPrime = True
		n = 0
		PCount = 0
		while checkPrime:
			x = n**2 + a*n + b
			#print x, isPrime(x), PCount, (a, b)
			if isPrime(x):
				PCount += 1
				n += 1
			else:
				if PCount > MaxLN:
					MaxLN = PCount
					maxA = a
					maxB = b
				checkPrime = False				
		print PCount, a, b, n, (n-1)**2 + a*(n-1) + b

print maxA*maxB

