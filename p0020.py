
def factorial(n):

	if n == 0:
		return 1
	else:
		return n*factorial(n-1)


x = str(factorial(100))

sum = 0
for i in range(len(x)):
	sum += int(x[i])

print sum
