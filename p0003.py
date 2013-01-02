
import numpy as num


def smallest_prime_fac(number,start):
	while start <= number:
		if number%start == 0:
			return start
		else:
			pass
		print start
		start += 2
	return

lim = 600851475143
#lim = 13195

primes = []
start = 3
while True:
	prime = smallest_prime_fac(lim,start)
	primes.append(prime)
	if primes[-1] != None:
		lim = lim/prime
		start = prime
	else:
		break
	
print primes

