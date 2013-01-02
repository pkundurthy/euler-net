
import numpy as num

def smallest_prime_fac(number,start):
	while start <= number:
		if number%start == 0:
			return start
		else:
			pass
		start += 1
	return

def all_prime_fac(number,start):
	primes = []
	while True:
		prime = smallest_prime_fac(number,start)
		primes.append(prime)
		if primes[-1] != None:
			number = number/prime
			start = prime
		else:
			break
	
	return primes[:-1]

number = 20
start = 2

num_array = num.arange(1,number+1,1)
lenx = number
print num_array
for i in range(lenx):
	ri = lenx-1-i
	x = num_array[ri]
	#print x,all_prime_fac(x,start)
	for prime in all_prime_fac(x,start):
		for j in range(lenx):
			rj = lenx-1-j
			if rj < ri:
				if num_array[rj]%prime == 0:
					num_array[rj] /= prime
		print num_array, prime, x
	
print num_array		

prod = 1
for el in num_array:
	prod *= el

print prod

