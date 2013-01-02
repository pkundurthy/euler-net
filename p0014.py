
def collatz(num):

	if num[-1] == 1:
		return num
	elif num[-1]%2 == 0:
		num.append(num[-1]/2)
		return collatz(num)
	else:
		num.append(3*num[-1] + 1)
		return collatz(num)



num = 1
longest = 0
lnum = 1
while num < 1000000:
	length = len(collatz([num]))
	if length > longest:
		longest = length
		lnum = num
	num += 1
	print num, length, longest

print lnum, longest

