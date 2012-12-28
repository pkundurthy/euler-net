import numpy as num

def isPalindromeCheck(number):

	diff = 99999999
	i = 0
	lennumber = len(number)
	isPalinDrome = True
	while diff >= 0: 
		outi = lennumber-(1+i)
		if number[i] != number[outi]:
			isPalinDrome = False
			break
		i += 1
		diff = outi-i

	return isPalinDrome


LargestProd = 0
for i in range(100,1000):
	for j in range(100,1000):
		prod = i*j
		if isPalindromeCheck(str(prod)):
			print i, j, i*j
			if prod > LargestProd:
				LargestProd = prod

print LargestProd

