sq = 20		   # the square grid
n = sq+1 	   # the point grid 
levels = 2*n-1 # the number of levels 

llist = []     # initiating an empty list

#looping through levels (better and a nested x,y loop)

for nlev in range(levels):
	#first element is 1
	if nlev == 0: llist = [1]

	# the level representing the diagonal of the grid
	newlist = []
	if nlev <= n-1:
		for j in range(nlev+1):
			# if first element - inherit previous first
			if j == 0:
				sumn = llist[j]
			# if last element - inherit previous last
			elif j == nlev:
				sumn = llist[j-1]
			# if in between, add the two above
			else:
				sumn = llist[j]+llist[j-1]
			newlist.append(sumn)
	else:
		for j in range(levels-(nlev)):
			# if first element - inherit previous first
			sumn = llist[j]+llist[j+1]
			newlist.append(sumn)
	print nlev, newlist
	llist = newlist
				
				





