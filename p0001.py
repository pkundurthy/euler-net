

sum = 0
for i in range(3,1000,1):
	if i%3 == 0 or i%5 == 0:
		print i
		sum += i

print sum
