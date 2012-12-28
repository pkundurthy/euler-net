

chaperone=''
digits = len(chaperone)
i = 1
while digits < 1e6:
	digits = len(chaperone)
	chaperone += str(i)
	if digits >= 1e0:
		d1 = int(chaperone[0])
	if digits >= 1e1:
		d2 = int(chaperone[9])
	if digits >= 1e2:
		d3 = int(chaperone[99])
	if digits >= 1e3:
		d4 = int(chaperone[999])
	if digits >= 1e4:
		d5 = int(chaperone[9999])
	if digits >= 1e5:
		d6 = int(chaperone[99999])
	if digits >= 1e6:
		d7 = int(chaperone[999999])
	i += 1

print d1*d2*d3*d4*d5*d6*d7


