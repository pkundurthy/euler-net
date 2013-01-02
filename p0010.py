
limit = 20
arr = [True]*limit

def sieve(x):
	global arr, limit
	for i in range(x*2, limit,x):
		arr[i] = False

map(sieve, range(2,limit/2) )
print sieve
primes= []
for i in range(2,limit):
	if arr[i]: primes.append(i)

sum = 0
for p in primes: sum += p
print sum
