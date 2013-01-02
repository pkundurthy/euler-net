
sum = 0
t = [1,2]
while t[1] <= 4000000:
	if t[1]%2 == 0:
		sum += t[1]
		print t, sum
	t = [t[1],t[1]+t[0]] 

print sum
