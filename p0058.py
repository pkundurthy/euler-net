

def isPrime(num):

	Out = True
	if num <= 1:
		Out = False
	elif num == 2:
		Out = True
	elif num % 2 == 0:
		Out = False
	else:
		s = 3
		while s*s <= num:
			if num%s == 0:
				Out = False
				break
			else:
				s += 2

	return Out


Side = 3
perc = 100.0

DPrime = []
DnonPrime = [1]

NPrime = 0
Nnon = 1
lastPrime = None
while True:
	BRSq = (Side)**2
	Sub1 = (Side) - 1
	BLSq = BRSq - Sub1
	TLSq = BRSq - 2*Sub1
	TRSq = BRSq - 3*Sub1

	for el in [BLSq,TRSq,TLSq]:
		if isPrime(el):
			NPrime += 1
			lastPrime = el
		else:
			Nnon += 1
	Nnon += 1

	lenTot = NPrime + Nnon
	perc = 100.*(NPrime)/(lenTot)
	print format(perc,'.2f'), Side, NPrime, lenTot, lastPrime
	#print DPrime
	#print DnonPrime

	Side += 2
	if Side > 7 and perc < 10.0:
		break

print Side

