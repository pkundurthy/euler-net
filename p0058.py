
def isPrime(number):

	Out = True
	if number%2 == 0:
		Out = False
	elif number < 0:
		Out = False
	elif number == 1:
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


Side = 1
perc = 100.0
CountUp = 1
x, y = 0, 0
dM = 0, 0


DPrime = []
DnonPrime = [1]

while True:
	BRSq = (Side)**2
	Sub1 = (Side) - 1
	BLSq = BRSq - Sub1
	TLSq = BRSq - 2*Sub1
	TRSq = BRSq - 3*Sub1
	SideStep = BRSq + 1
	
	if CountUp == SideStep:
		dM = (0,1)
		Side += 2
	elif CountUp == TRSq:
		dM = (-1,0)
	elif CountUp == TLSq:
		dM = (0,-1)
	elif CountUp == BLSq:
		dM = (1,0)
	else:
		pass

	#print CountUp, x, y, Side, dM, (BRSq,TRSq,TLSq,BLSq,SideStep)

	if x == y or -1*x == y:
		Corner = True
		if isPrime(CountUp):
			DPrime.append(CountUp)
		else:
			DnonPrime.append(CountUp)
	else:
		Corner = False

	lenPr = len(DPrime)
	lenNon = len(DnonPrime)
	lenTot = lenPr + lenNon
	perc = 100.*(lenPr)/(lenTot)
	if Corner: 
		print format(perc,'.2f'), Side, lenPr, lenTot
		#print DPrime
		#print DnonPrime
		pass

	if CountUp != 1:
		x = x+dM[0]
		y = y+dM[1]
	else:
		x += 1
	CountUp += 1

	#print perc, lenPr, lenTot, Sid

	if Side > 7 and perc < 10.0:
		break

