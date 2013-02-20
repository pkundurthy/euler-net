
Side = 1001
Top = Side**2

x,y = (Side-1)/2,(Side-1)/2
Lev = Side
CDown = Top
SumD = 0 

TR, TL, BR, BL = None, None, None, None
dM = 0, 0
while CDown > 0:

	TopSq = (Lev)**2
	Sub1 = (Lev) - 1
	TLSq = TopSq - Sub1
	BLSq = TopSq - 2*Sub1
	BRSq = TopSq - 3*Sub1
	EndSq = TopSq - 4*Sub1 + 1

	if CDown == TopSq:
		dM = (-1,0)
	elif CDown == TLSq:
		dM = (0,-1)
	elif CDown == BLSq:
		dM = (1,0)
	elif CDown == BRSq:
		dM = (0,1)
	elif CDown == EndSq:
		dM = (-1,0)
		Lev -= 2

	#print CDown, x, y, Lev, dM, (TopSq,TLSq,BLSq,BRSq,EndSq)

	if x == y and x > 0 and y > 0:
		SumD += CDown
		Corner = True
	elif -1*x == y and x < 0 and y > 0:
		SumD += CDown
		Corner = True
	elif x == y and x < 0 and y < 0:
		SumD += CDown
		Corner = True
	elif -1*x == y and x > 0 and y < 0:
		SumD += CDown
		Corner = True
	else:
		Corner = False


	if Corner: print SumD, CDown, x, y

	x = x+dM[0]
	y = y+dM[1]
	CDown -= 1



print SumD+1


