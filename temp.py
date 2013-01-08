sq = 1000	   # the square grid
n = sq+1 	   # the point grid 
levels = 2*n-1 # the number of levels 

llist = []     # initiating an empty list

#looping through levels (better and a nested x,y loop)

def checkSq(x,y):
	isSQ = False
	sqrx = x**(0.5)
	sqry = y**(0.5)
	sqrxy = (x+y)**(0.5)
	if x == 0 or y == 0 or x == 1 or y == 1:
		pass
	elif int(sqrx) == sqrx and \
	   int(sqry) == sqry and \
	   int(sqrxy) == sqrxy:
		#print x, y, x+y
		isSQ = True
	else:
		pass
	return isSQ

for nlev in range(levels):
	#first element is 1
	if nlev == 0: llist = [1]

	# the level representing the diagonal of the grid
	newlist = []
	if nlev <= n-1:
		for j in range(nlev+1):
			# if first element - inherit previous first
			x = j
			y = nlev-x
			if j == 0:
				sumn = llist[j]
			# if last element - inherit previous last
			elif j == nlev:
				sumn = llist[j-1]
			# if in between, add the two above
			else:
				sumn = llist[j]+llist[j-1]

			if checkSq(x,y):
				newlist.append(0)
			else:
				newlist.append(sumn)
			#print nlev, x, y
	else:
		for j in range(levels-(nlev)):
			y = n-1-j
			x = nlev-y
			
			# if first element - inherit previous first
			sumn = llist[j]+llist[j+1]
			if checkSq(x,y):
				newlist.append(0)
			else:
				newlist.append(sumn)
			#print nlev, x, y
	
	#print nlev, newlist
	print nlev+1, levels-nlev, levels
	llist = newlist

print llist[0]%1000000007	
				





