
def smallest_prime_fac(number,start):
	while start <= number:
		if number%start == 0:
			return start
		else:
			pass
		start += 2
	return

count = 2
num = 3
maxnum = 10001
while count < maxnum+1:
	smallest_p = smallest_prime_fac(num,3)
	if smallest_p != None and smallest_p == num:
		print num, count
		count += 1	

	if count != maxnum+1:
		num += 2

print num
